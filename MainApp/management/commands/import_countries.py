import json
from django.core.management.base import BaseCommand
from MainApp.models import Country, Language

class Command(BaseCommand):
    help = "Импорт стран и языков из countries.json в БД"

    def handle(self, *args, **kwargs):
        with open('countries.json', encoding='utf-8') as f:
            countries = json.load(f)

        for country_data in countries:
            country_name = country_data.get("country")
            languages_list = country_data.get("languages", [])

            if not country_name:
                continue

            # 1. Creează / actualizează țara
            country, _ = Country.objects.get_or_create(name=country_name)

            # 2. Creează limbile și le leagă de țară
            for lang_name in languages_list:
                lang, _ = Language.objects.get_or_create(name=lang_name)
                country.languages.add(lang)

        self.stdout.write(self.style.SUCCESS("✅ Țările și limbile au fost importate"))

