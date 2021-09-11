from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('invoice/', views.invoice),
    path('profile/', views.profile),
]
