import importlib

from django.conf import settings
from django.core.management.base import BaseCommand

from django_doc_view import django_doc_view


class Command(BaseCommand):
    help = 'document'  # TODO

    def handle(self, *args, **options):
        urlpatterns = importlib.import_module(
            settings.ROOT_URLCONF
        ).urlpatterns
        result = django_doc_view(urlpatterns)
        print(result)
