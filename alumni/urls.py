from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('news/', views.news_list, name='news_list'),
    path('achievements/', views.achievements_list, name='achievements_list'),
    path('alumni/', views.alumni_list, name='alumni_list'),
]
