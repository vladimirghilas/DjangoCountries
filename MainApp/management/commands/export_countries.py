import os
import json
from django.core.management.base import BaseCommand
from MainApp.models import Country


class Command(BaseCommand):
    help = "Экспорт стран из БД в countries.json"

    def handle(self, *args, **kwargs):
        output_dir = "MainApp/management/fixtures"
        os.makedirs(output_dir, exist_ok=True)

        output_file = os.path.join(output_dir, "countries.json")
        countries = list(Country.objects.values())

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(countries, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS(f"Данные успешно экспортированы в {output_file}"))