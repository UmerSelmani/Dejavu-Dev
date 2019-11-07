
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^sign_up', views.home, name="home"),
    url(r'^sign_in$', views.signin, name='Sign-In')
]
