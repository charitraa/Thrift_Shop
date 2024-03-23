from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.HomePage, name="Home"),
    path('login/', views.login, name="login"),
    path('card/', views.card, name="card"),
    path('incard/',views.incard, name="incard"),
    path('form/',views.form, name="form"),
]

