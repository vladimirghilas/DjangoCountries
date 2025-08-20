import json
from django.core.management.base import BaseCommand
from MainApp.models import Country

class Command(BaseCommand):
    help = "Импорт стран из countries.json в БД"

    def handle(self, *args, **kwargs):
        with open('countries.json', encoding='utf-8') as f:
            countries = json.load(f)

        for country in countries:
            country_name = country.get("country")
            languages = country.get('languages', [])
            if country_name:
                Country.objects.update_or_create(
                    name = country_name,
                    defaults={'languages': languages}
                )
        self.stdout.write(self.style.SUCCESS(" Страны успешно импортированы"))

