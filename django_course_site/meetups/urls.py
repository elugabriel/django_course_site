from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'), # our-domain.com/meetups
  ]