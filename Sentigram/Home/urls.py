from django.urls import path
from . import views

urlpatterns = [
    path('company', views.company, name='company'),
    path('result/', views.result, name='result'),
    path('', views.home, name='home'),
]
