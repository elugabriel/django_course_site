from django.urls import path
from . import views

urlpatterns = [
    path('meetups', views.index), #our main domain
    path('meetups/<meetup_slug>'), #our-domain.com/meetups/<dynamic-path-segment> 
  ]