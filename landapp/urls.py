from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('land/', views.land, name='land'),
    path('land_details/<slug:slug>/', views.land_details, name='land_details'),
]


