from django.urls import path
from . import views

urlpatterns = [
    path('', views.realtors, name="realtors"),
    path('realtor/<str:pk>/', views.realtor, name="realtor"),
    path('cottage/', views.create_cottage, name="cottage"),


]