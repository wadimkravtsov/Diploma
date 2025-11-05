from django.urls import path
from . import views

urlpatterns = [
    path('', views.realtors, name="realtors"),
    path('realtor/<str:pk>/', views.realtor, name="realtor"),
    path('cottage/', views.create_cottage, name="cottage"),
    path('update_cottage/<str:pk>/', views.update_cottage, name="update_cottage"),
    path('delete_cottage/<str:pk>/', views.delete_cottage, name="delete_cottage"),
]