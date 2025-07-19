import os
import json
from django.conf import settings
from django.shortcuts import render
from django.utils.text import slugify
from django.http import Http404

def load_countries_data():
    path_json = os.path.join(settings.BASE_DIR, 'countries.json')
    with open(path_json,'r', encoding='utf-8') as file:
        countries = json.load(file)
        
        for country in countries:
            country['slug'] = slugify(country.get('country', ''))

    return countries
def home_views(request):
    return render(request, 'MainApp/home.html')

def countries_view(request):
    countries = load_countries_data()
    return render(request, 'MainApp/countries.html', {'countries': countries})

def country_detail(request, slug):
    countries = load_countries_data()

    for country in countries:
        if country['slug'] == slug:
            slugify_country = country
            break
    else:
        raise  Http404("Страна не найдена")

    return render(request,'MainApp/country_detail.html',{'country': slugify_country} )

def languages_view(request):
    countries = load_countries_data()

    languages = set()
    for country in countries:
        langs = country.get('languages', [])
        for lang in langs:
            if lang:
                languages.add(lang.strip())
    languages_list = sorted(languages)

    return render(request, 'MainApp/lang.html', {'languages': languages_list})