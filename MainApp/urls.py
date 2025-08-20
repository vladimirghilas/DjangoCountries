from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('about/',views.about_view, name='about'),
    path('', views.home_views, name='home'),
    path('countries/list/', views.countries_view, name='countries-list'),
    path('countries/languages/', views.languages_view, name='languages-list'),
    path('countries/<str:country_name>/', views.country_detail, name='country-detail'),

]
