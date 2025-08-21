from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('', views.home_views, name='home'),
    path('countries/list/', views.countries_view, name='countries-list'),
    path('countries-by/<str:letter>/', views.countries_view, name='countries-by-letter'),
    path('languages/list', views.languages_view, name='languages-list'),
    path('languages-by/<str:letter>/', views.languages_view, name='languages-by-letter'),
    path('languages/<str:country_name>/', views.country_detail, name='country-languages'),
    path('countries/<str:language_name>/', views.language_detail, name='language-countries'),

]
