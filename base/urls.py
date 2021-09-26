from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('send/', views.sendNotifications, name='SendNotifications'),


]