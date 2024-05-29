from django import views
from django.urls import path
from . import views as users_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register',users_view.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',users_view.logout, name='logout')

]
