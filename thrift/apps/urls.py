from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup,name="signup" ),
    path('', views.HomePage, name="Home"),
    path('login/', views.login, name="login"),
    path('card/', views.card, name="card"),
    path('incard/',views.incard, name="incard"),
    path('form/',views.form, name="form"),
    path('profile/',views.profile, name="profile"),

]

