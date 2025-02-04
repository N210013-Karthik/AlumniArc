from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import NewsPage, Achievement, Alumni, Event
from django.db.models import Q  # For searching
from django.utils.timezone import now

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
    news = NewsPage.objects.filter(is_published=True)
    events = Event.objects.all()
    
    upcoming_events = [event for event in events if event.is_upcoming()]
    
    return render(request, 'homepage.html', {'news': news, 'events':upcoming_events})

def news_list(request):
    query = request.GET.get('q', '')  # Search query
    category_filter = request.GET.get('category', 'All')  # Category filter

    news = NewsPage.objects.filter(is_published=True)

    if query:
        news = news.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if category_filter and category_filter != 'All':
        news = news.filter(category=category_filter)

    categories = ['All', 'Event', 'Achievement', 'General']  # Available categories

    return render(request, 'newspage.html', {'news': news, 'categories': categories, 'query': query, 'category_filter': category_filter})

def achievements_list(request):
    query = request.GET.get('q')  # Search query
    category_filter = request.GET.get('category')  # Category filter

    achievements = Achievement.objects.filter(is_approved=True)

    if query:
        achievements = achievements.filter(Q(title__icontains=query) | Q(description__icontains=query))

    if category_filter and category_filter != 'All':
        achievements = achievements.filter(category=category_filter)

    # Separate achievements into past and present based on the is_present method
    present_achievements = [ach for ach in achievements if ach.is_present()]
    past_achievements = [ach for ach in achievements if not ach.is_present()]

    categories = ['All', 'Academics', 'Sports', 'Research', 'Entrepreneurship', 'Others']

    return render(request, 'Achievements.html', {
        'present_achievements': present_achievements, 
        'past_achievements': past_achievements, 
        'categories': categories
    })

def alumni_list(request):
    query = request.GET.get('q')  # Search query
    department_filter = request.GET.get('department')  # Filter by department
    graduation_year_filter = request.GET.get('graduation_year')  # Filter by graduation year

    alumni = Alumni.objects.all()

    # Search query (matches name, position, company, location, skills, achievements)
    if query:
        alumni = alumni.filter(
            Q(name__icontains=query) | 
            Q(current_position__icontains=query) | 
            Q(company__icontains=query) |
            Q(location__icontains=query) |
            Q(skills__icontains=query) |  # Searches inside JSON skills array
            Q(achievements__icontains=query)  # Searches inside JSON achievements array
        )

    # Filter by department
    if department_filter and department_filter != 'All':
        alumni = alumni.filter(department=department_filter)

    # Filter by graduation year
    if graduation_year_filter and graduation_year_filter != 'All':
        alumni = alumni.filter(graduation_year=graduation_year_filter)

    # Unique departments and graduation years
    departments = ['All', 'CSE', 'ECE', 'EEE', 'ME', 'CE', 'CHEM', 'MME', 'Others']
    graduation_years = sorted(set(Alumni.objects.values_list('graduation_year', flat=True)), reverse=True)

    return render(request, 'AlumniDirectory.html', {
        'alumni': alumni,
        'departments': departments,
        'graduation_years': graduation_years
    })

def event_list(request):
    """
    This view will display the list of events with optional search and filter functionality.
    """

    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    # Get all events
    events = Event.objects.all()

    # Apply search filter
    if query:
        events = events.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(category__icontains=query)
        )

    # Apply category filter
    if category:
        events = events.filter(category=category)

    # Apply date range filter
    if start_date:
        events = events.filter(start_date__gte=start_date)
    if end_date:
        events = events.filter(start_date__lte=end_date)

    # Separate events into upcoming, past, and ongoing
    current_time = now()
    upcoming_events = events.filter(start_date__gt=current_time)
    past_events = events.filter(start_date__lt=current_time)
    ongoing_events = events.filter(start_date__lte=current_time, updated_at__gte=current_time)  # Assuming updated_at is used as event end time

    return render(request, 'events page.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'ongoing_events': ongoing_events
    })

def about_view(request):
    return render(request, 'aboutPage.html')