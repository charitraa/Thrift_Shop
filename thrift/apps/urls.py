from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', views.signup,name="signup" ),
    path('', views.HomePage, name="Home"),
    path('login/', views.login, name="login"),
    path('incard/<int:product_id>/',views.incard, name="incard"),
    path('customer/<int:id>/',views.CustomerPage, name="customer"),
    path('cart/<int:cart_id>',views.cart, name="cart"),
    path('profile/',views.profile, name="profile"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    



