from django.urls import path
from django.contrib import admin
from netbalanceApp import views

# gets imported into netbalanceProject\urls.py
urlpatterns = [
    path('', views.login, name='login'),
    path('admin', admin.site.urls),
    path('register', views.register, name='register'),
    path('homepage', views.homepage, name='homepage'),
    path('mission', views.mission, name='mission'),
    path('dashboardv2', views.dashboardv2, name='dashboardv2'),
    path('dashboardv3', views.dashboardv3, name='dashboardv3'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
