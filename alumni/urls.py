from django.urls import path
from . import views
from django.urls import path
from .views import logout_view

urlpatterns = [
    path('login/', views.login_view,name='login_page'),
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
    
    path('dashboard/achievements/', views.achievement_view, name='achievements'),
    path('dashboard/achievement/add/', views.create_or_edit_achievement, name='add_achievement'),
    path('dashboard/achievement/edit/<int:achievement_id>/', views.create_or_edit_achievement, name='edit_achievement'),
    path('dashboard/achievement/delete/<int:achievement_id>/', views.delete_achievement, name='delete_achievement'),
    
    path('dashboard/opportunities/', views.opportunity_view, name='dopportunities'),
    path('dashboard/opportunity/add/', views.create_or_edit_opportunity, name='add_opportunity'),
    path('dashboard/opportunity/edit/<int:opportunity_id>/', views.create_or_edit_opportunity, name='edit_opportunity'),
    path('dashboard/opportunity/delete/<int:opportunity_id>/', views.delete_opportunity, name='delete_opportunity'),
    
    path('dashboard/alumni/', views.alumni_view, name='alumni'),
    path('dashboard/alumni/add/', views.create_or_edit_alumni, name='add_alumni'),
    path('dashboard/alumni/edit/<int:alumni_id>/', views.create_or_edit_alumni, name='edit_alumni'),
    path('dashboard/alumni/delete/<int:alumni_id>/', views.delete_alumni, name='delete_alumni'),
    
    path('dashboard/news/', views.news_view, name='news'),
    path('dashboard/news/add/', views.create_or_edit_news, name='add_news'),
    path('dashboard/news/edit/<int:news_id>/', views.create_or_edit_news, name='edit_news'),
    path('dashboard/news/delete/<int:news_id>/', views.delete_news, name='delete_news'),
    
    path('dashboard/events/', views.event_view, name='events'),
    path('dashboard/event/add/', views.create_or_edit_event, name='add_event'),
    path('dashboard/event/edit/<int:event_id>/', views.create_or_edit_event, name='edit_event'),
    path('dashboard/event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
