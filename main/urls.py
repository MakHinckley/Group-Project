from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('welcome', views.welcome),
    path('login', views.login),
    path('logout',views.logout),
    path('registerPage', views.registerPage),
    path('gamePage', views.gamePage),
    path('recently_played', views.recently_played),
    path('admin/', admin.site.urls),
]