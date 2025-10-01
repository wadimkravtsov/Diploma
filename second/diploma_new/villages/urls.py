from django.urls import path
from . import views

urlpatterns = [
    path('', views.villages, name="villages"),
    path('village/<str:pk>/', views.village, name="village"),

]