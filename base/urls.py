#file to store urls for apps
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/<str:pk>', views.userProfile, name="user-profile"),
    path('', views.home, name="home"),
    path('database/<str:pk>', views.database, name="database"),
    path('about/<str:pk>', views.aboutpage, name="about"),
    path('database-form/', views.databaseForm, name="database-form")
]