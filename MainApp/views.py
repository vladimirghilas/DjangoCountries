from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from MainApp.models import Country, Language


def about_view(request):
    return render(request, 'about.html')


def home_views(request):
    return render(request, 'home.html')


def countries_view(request, letter=None):
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if letter:
        countries_list = Country.objects.filter(name__startswith=letter).order_by('name')
    else:
        countries_list = Country.objects.all().order_by('name')  # все страны из БД
        # пагинация (10 стран на страницу)
    paginator = Paginator(countries_list, 9)
    page_number = request.GET.get("page")  # номер страницы из query params ?page=2
    countries = paginator.get_page(page_number)

    context = {
        'countries': countries,
        "letters": letters,
        "selected_letter": letter
    }
    return render(request, 'countries.html', context)


def country_detail(request, country_name):
    country = get_object_or_404(Country, name=country_name)
    return render(request, 'country_languages.html', {'country': country})


def languages_view(request, letter=None):
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if letter:
        languages_list = Language.objects.filter(name__startswith=letter).order_by('name')
    else:
        languages_list = Language.objects.all().order_by('name')

    paginator = Paginator(languages_list, 6)
    page_number = request.GET.get("page")  # номер страницы из query params ?page=2
    languages = paginator.get_page(page_number)

    context = {
        "letters": letters,
        'languages': languages,
        "selected_letter": letter
    }
    return render(request, 'languages.html', context)


def language_detail(request, language_name):
    language = get_object_or_404(Language, name=language_name)
    return render(request, 'language_countries.html', {'language': language})
