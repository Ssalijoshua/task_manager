from django.urls import path
from django.contrib import admin
from django.urls import include
from django.views.generic import TemplateView
from . import views

app_name = 'tasks' # This is for namespacing the URLs
urlpatterns = [
    path('', TemplateView.as_view(template_name='tasks/home.html'), name='home'),
    path('help/', TemplateView.as_view(template_name='tasks/help.html'), name='help'),
    path('', views.home, name='home'),  # Home page
    path('help/', views.help, name='help'),  # Help page
    path('about/', views.about, name='about'),
]