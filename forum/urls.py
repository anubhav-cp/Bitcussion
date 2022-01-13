from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('questons/<str:pk>/<str:ck>/', views.solutionPage, name='solution')
]