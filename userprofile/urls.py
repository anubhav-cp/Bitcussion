from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.accountPage, name='account'),
    path('edit-profile/', views.updateAccountPage, name='update-account'),
]