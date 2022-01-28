from django.urls import path , include
from . import views
from knox import views as knox_views

urlpatterns = [
    path('recipe', views.home),
    path('lunch', views.lunch),
    path('dinner', views.dinner),
    path('snacks', views.snacks),
    path('breakfast', views.breakfast),
    
    path('recipe/<int:pk>', views.recipeDetail),
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]