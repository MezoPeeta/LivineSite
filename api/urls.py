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
    path('recipeType/<str:type>', views.recipeTypeDetail),
    path('types/', views.recipe_all_types),

    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('user/<int:pk>', views.get_users, name='Users'),

    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]