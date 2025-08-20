from django.shortcuts import render, get_object_or_404
from MainApp.models import Country, Language


def about_view(request):
    return render(request, 'about.html')
def home_views(request):
    return render(request, 'home.html')

def countries_view(request):
    countries = Country.objects.all().order_by('name')  # все страны из БД
    return render(request, 'countries.html', {'countries': countries})

def country_detail(request, country_name):
    country = get_object_or_404(Country, name=country_name)
    return render(request, 'country_detail.html', {'country': country})

def languages_view(request):
    # Luăm toate limbile din DB
    languages = Language.objects.all().prefetch_related('countries').order_by('name')

    return render(request, 'lang.html', {'languages': languages})