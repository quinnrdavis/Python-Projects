from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profiles_page', views.profiles_page, name="profiles_page"),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('confirmdelete/', views.confirm, name="confirm"),
    path('createRecord', views.createRecord, name="createRecord"),
]