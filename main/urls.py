from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('users/create', views.create_user),
    path('welcome', views.welcome),
    path('users/login', views.login),
    path('logout',views.logout),
    path('recently_played', views.recently_played),
]