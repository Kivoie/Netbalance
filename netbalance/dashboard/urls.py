from django.urls import path
from . import views

urlpatterns = [
        #path('', views.template_base, name='template_base'),
        path('', views.template_dashboard, name='template_dashboard'),
        path('settings', views.template_settings, name='template_settings')
]
