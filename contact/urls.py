from django.urls import path
from . import views
urlpatterns = [
    path('contact_page/', views.contact_page, name='contact_page'),
]