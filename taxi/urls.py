from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signupform',views.signupform, name='signupform'),
    path('loginform',views.loginform, name='loginform'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('reset',views.reset, name='reset')
]