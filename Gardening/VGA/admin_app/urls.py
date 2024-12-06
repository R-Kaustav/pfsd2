from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [

    path('', views.WelcomePage, name='WelcomePage'),  # Ensure this is the root
    path('user_app/', views.userprojecthomepage, name='UserProjectHomePage'),

    path('project/', views.projecthomepage, name='projecthomepage'),
    path('login/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('login_logic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('register/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('register_logic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('logout/', views.logout_view, name='logout'),
    path('seller/', views.seller_homepage, name='sellerhomepage'),
]
