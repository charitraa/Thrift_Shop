from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', views.signup,name="signup" ),
    path('', views.HomePage, name="Home"),
    path('login/', views.login, name="login"),
    path('card/', views.card, name="card"),
    path('incard/',views.incard, name="incard"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
