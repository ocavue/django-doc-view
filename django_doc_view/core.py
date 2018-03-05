import django
from collections import namedtuple

version = django.get_version().split('.', maxsplit=3)

if version[0] == '1':
    # https://stackoverflow.com/a/35760156/9426588
    from django.core.urlresolvers import (
        RegexURLResolver as URLResolver, RegexURLPattern as URLPattern
    )
elif version[0] == '2':
    from django.urls import URLResolver, URLPattern
else:
    raise Exception(
        'unknown django version. django-doc-view only support django 1.x and 2.x. Welcome pull request.'
    )

DEFAULT_OUTPUT_FORMAT = '''## {route}
    {doc}
'''

DEFAULT_SKIP_VIEW_NAMES = (
    'serve', 'add_view', 'change_view', 'changelist_view', 'history_view', 'delete_view',
    'RedirectViewInfo'
)

ViewInfo = namedtuple('ViewInfo', ['route', 'url_pattern'])


def __get_route(url_pattern):
    try:
        # for django 2.x
        return url_pattern.pattern._route  # TODO remove private attribute
    except Exception:
        pass

    try:
        # for django 2.x
        return url_pattern.pattern._regex  # private attribute
    except Exception:
        pass

    try:
        # for django 1.x
        return url_pattern._regex  # private attribute
    except Exception:
        pass

    raise Exception('unknow url_pattern')


def __get_all_view_infos(urlpatterns):
    view_infos = []

    for url_pattern in urlpatterns:
        if isinstance(url_pattern, URLResolver):
            url_resolver = url_pattern

            prefix = __get_route(url_resolver)
            view_infos += [
                ViewInfo(
                    route=prefix + view.route,
                    url_pattern=view.url_pattern,
                ) for view in __get_all_view_infos(url_resolver.url_patterns)
            ]

        elif isinstance(url_pattern, URLPattern):
            view_infos.append(ViewInfo(
                route=__get_route(url_pattern),
                url_pattern=url_pattern,
            ))

        else:
            raise Exception('unknown url_pattern type {}'.format(type(url_pattern)))

    return view_infos


def django_doc_view(
    all_urlpatterns,
    output_format=DEFAULT_OUTPUT_FORMAT,
    skip_view_names=DEFAULT_SKIP_VIEW_NAMES,
):
    # TODO add docstring
    view_infos = [
        i for i in __get_all_view_infos(all_urlpatterns)
        if i.url_pattern.callback.__name__ not in skip_view_names
    ]

    return '\n'.join(
        [
            output_format.format(
                route=i.route,
                doc=i.url_pattern.callback.__doc__,
            ) for i in view_infos
        ]
    )
