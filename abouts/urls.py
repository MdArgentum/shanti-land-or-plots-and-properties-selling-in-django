# This code is defining a URL pattern for the Django web framework.
from django.urls import path
from . import views
urlpatterns = [
    path('about_page/', views.about_page, name='about_page'),
]