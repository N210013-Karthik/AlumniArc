from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('news/', views.news_list, name='news_list'),
    path('achievements/', views.achievements_list, name='achievements_list'),
    path('alumni/', views.alumni_list, name='alumni_list'),
    path('events/', views.event_list, name='event_list'),
    path('opportunities/', views.opportunity_list, name='opportunities'),
    path('donations/', views.donation_view, name='donations'),
    path('about/', views.about_view, name='about'),
]
