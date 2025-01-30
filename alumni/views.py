from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import NewsPage
from django.db.models import Q  # For searching

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def homepage_view(request):
    return render(request, 'homepage.html')

def news_list(request):
    query = request.GET.get('q')  # Search query
    category_filter = request.GET.get('category')  # Category filter

    news = NewsPage.objects.filter(is_published=True)

    if query:
        news = news.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if category_filter and category_filter != 'All':
        news = news.filter(category=category_filter)

    categories = ['All', 'Event', 'Achievement', 'General']  # Available categories

    return render(request, 'newspage.html', {'news': news, 'categories': categories})