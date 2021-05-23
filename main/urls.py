from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('welcome', views.welcome),
    path('login', views.login),
    path('logout',views.logout),
    path('users/create', views.create_user),
    path('registerPage', views.registerPage),
    path('users/login', views.login),
    path('welcome', views.welcome),
    path('recently_played', views.recently_played),
    path('logout',views.logout),
    path('admin/', admin.site.urls),
    
]