from django.urls import path
from . import views
from django.urls import path
from .views import logout_view

urlpatterns = [
    path('login/',views.login_view,name='login_page'),
    path('', views.homepage_view, name='homepage'),
    path('news/', views.news_list, name='news_list'),
    path('achievements/', views.achievements_list, name='achievements_list'),
    path('alumni/', views.alumni_list, name='alumni_list'),
    path('events/', views.event_list, name='event_list'),
    path('opportunities/', views.opportunity_list, name='opportunities'),
    path('donations/', views.donation_view, name='donations'),
    path('about/', views.about_view, name='about'),
    path('logout/', logout_view, name='logout'),
    
    # Admin URLs
    
    path('dashboard/', views.dashboard, name='dashboard'),
]
