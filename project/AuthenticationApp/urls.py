from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('authentication/signup', views.signup, name="signup"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    
    path('authentication/signin/', views.signin, name="signin"),
    path('authentication/signoutHome/', views.signoutHome, name="signoutHome"),

    

]
