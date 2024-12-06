from django.urls import path
from . import views

app_name = 'user_app'  # This sets the namespace for the app
urlpatterns = [
    path('homepage/', views.UserProjectHomePage, name='userprojecthomepage'),
    path('get_weather/', views.get_weather, name='get_weather'),
    path('weatherintegration/', views.weatherintegration, name='weatherintegration'),
    path('get-weather/', views.get_weather, name='get_weather'),
]
#weatherintegration