from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='MainApp/about.html'), name='about'),
    path('', views.home_views, name='home'),
    path('countries/list/', views.countries_view, name='countries-list'),
    path('countries/languages/', views.languages_view, name='languages-list'),
    path('countries/<slug:slug>/', views.country_detail, name='country-detail'),

]
