from django.contrib import admin
from django.urls import path
# skomunikowanie z metodą w views.py:
from password_generator_app import views

app_name = 'password_generator'

urlpatterns = [
    path ('', views.home, name="home"),
    path ('aboutme', views.aboutme, name="aboutme"),
    path ('passwordo/', views.passwordo, name="passwordo"),

]
