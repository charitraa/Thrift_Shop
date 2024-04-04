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
    path('addcart/<int:id>/<int:product_id>/', views.addcart, name="cart"),
    path('cart/<int:id>/', views.cart, name="cart"),
    path('profile/<int:profile_id>',views.profile, name="profile"),
    path('items/<int:items_id>',views.items, name="items"),
    path('itemedit/<int:product_id>',views.editItem, name="edititem"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




