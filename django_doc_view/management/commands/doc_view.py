import importlib

from django.conf import settings
from django.core.management.base import BaseCommand

from django_doc_view import django_doc_view
from django_doc_view.core import DEFAULT_OUTPUT_FORMAT


class Command(BaseCommand):
    help = (
        'The simplest way to document your Django APIs. '
        'read this page for more information: https://github.com/ocavue/django-doc-view'
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--format',
            required=False,
            type=str,
            help='use custom format to replace default format: "{}"'.format(
                DEFAULT_OUTPUT_FORMAT.replace('\n', '\\n')
            ),
        )

    def handle(self, *args, **options):
        urlpatterns = importlib.import_module(settings.ROOT_URLCONF).urlpatterns
        if options.get('format'):
            result = django_doc_view(
                urlpatterns, output_format=options['format'].replace('\\n', '\n')
            )
        else:
            result = django_doc_view(urlpatterns)
        print(result)
