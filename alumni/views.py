from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . import forms, models
from django.db.models import Q  # For searching
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@csrf_exempt

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to home after logout


def homepage_view(request):
    news = models.NewsPage.objects.filter(is_published=True)
    events = models.Event.objects.all()
    
    upcoming_events = [event for event in events if event.is_upcoming()]
    
    return render(request, 'homepage.html', {'news': news, 'events':upcoming_events})


def news_list(request):
    query = request.GET.get('q', '')  # Search query
    category_filter = request.GET.get('category', 'All')  # Category filter

    news = models.NewsPage.objects.filter(is_published=True)

    if query:
        news = news.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if category_filter and category_filter != 'All':
        news = news.filter(category=category_filter)

    categories = ['All', 'Event', 'Achievement', 'General']  # Available categories

    return render(request, 'newspage.html', {'news': news, 'categories': categories, 'query': query, 'category_filter': category_filter})

def achievements_list(request):
    query = request.GET.get('q')  # Search query
    category_filter = request.GET.get('category')  # Category filter

    achievements = models.Achievement.objects.filter(is_approved=True)

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

    alumni = models.Alumni.objects.all()

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
    graduation_years = sorted(set(models.Alumni.objects.values_list('graduation_year', flat=True)), reverse=True)

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
    events = models.Event.objects.all()

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

def opportunity_list(request):
    query = request.GET.get('q', '')
    opportunity_type = request.GET.get('opportunity_type', '')

    opportunities = models.Opportunity.objects.all()

    if query:
        opportunities = opportunities.filter(
            Q(title__icontains=query) | 
            Q(company__icontains=query) |
            Q(description__icontains=query)
        )

    if opportunity_type:
        opportunities = opportunities.filter(opportunity_type=opportunity_type)

    return render(request, 'opportunities.html', {
        'opportunities': opportunities,
        'query': query,
        'opportunity_type': opportunity_type
    })

def donation_view(request):
    return render(request, 'donation.html')

def about_view(request):
    return render(request, 'about page.html')


# Admin views

@login_required(login_url='/login/')
def dashboard(request):
    total_alumni = models.Alumni.objects.count()
    upcoming_events_count = models.Event.objects.filter(start_date__gt=now()).count()
    opportunities_count = models.Opportunity.objects.count()
    current_user = request.user

    context = {
        'total_alumni': total_alumni,
        'upcoming_events_count': upcoming_events_count,
        'opportunities_count': opportunities_count,
        'current_user': current_user,
    }

    return render(request, 'admin/dashboard.html', context)

@login_required(login_url='/login/')
def achievement_view(request):
    achievement_list = models.Achievement.objects.all()
    current_user = request.user
    return render(request, 'admin/achievements_view.html', {'achievements': achievement_list, 'current_user': current_user})

@login_required(login_url='/login/')
def create_or_edit_achievement(request, achievement_id=None):
    current_user = request.user
    if achievement_id:
        achievement = models.Achievement.objects.get(id=achievement_id)
        if request.method == 'POST':
            form = forms.AchievementForm(request.POST, request.FILES, instance=achievement)
            if form.is_valid():
                achievement = form.save(commit=False)
                achievement.save()
                return redirect('/dashboard/achievements/')
        else:
            form = forms.AchievementForm(instance=achievement)
        return render(request, 'admin/achievementsform.html', {'form': form, 'achievement': achievement, 'current_user': current_user, 'errors': form.errors})   
    else:
        if request.method == 'POST':
            form = forms.AchievementForm(request.POST, request.FILES)
            if form.is_valid():
                achievement = form.save(commit=False)
                achievement.save()
                return redirect('/dashboard/achievements/')
        else:
            form = forms.AchievementForm()

    return render(request, 'admin/achievementsform.html', {'form': form, 'current_user': current_user, 'errors': form.errors})

@login_required(login_url='/login/')
def delete_achievement(request, achievement_id):
    achievement = models.Achievement.objects.get(id=achievement_id)
    achievement.delete()
    return redirect('/dashboard/achievements/')

@login_required(login_url='/login/')
def opportunity_view(request):
    opportunity_list = models.Opportunity.objects.all()
    current_user = request.user
    return render(request, 'admin/opportunities_view.html', {'opportunities': opportunity_list, 'current_user': current_user})

@login_required(login_url='/login/')
def create_or_edit_opportunity(request, opportunity_id=None):
    current_user = request.user
    if opportunity_id:
        opportunity = models.Opportunity.objects.get(id=opportunity_id)
        if request.method == 'POST':
            form = forms.OpportunityForm(request.POST, request.FILES, instance=opportunity)
            if form.is_valid():
                print("Form is valid")
                opportunity = form.save(commit=False)
                opportunity.save()
                return redirect('/dashboard/opportunities/')
        else:
            form = forms.OpportunityForm(instance=opportunity)
        return render(request, 'admin/opportunities_dashboard.html', {'form': form, 'opportunity': opportunity, 'current_user': current_user, 'errors': form.errors})   
    else:
        if request.method == 'POST':
            form = forms.OpportunityForm(request.POST, request.FILES)
            if form.is_valid():
                opportunity = form.save(commit=False)
                opportunity.posted_by = current_user
                opportunity.save()
                return redirect('/dashboard/opportunities/')
        else:
            form = forms.OpportunityForm()

    return render(request, 'admin/opportunities_dashboard.html', {'form': form, 'current_user': current_user, 'errors': form.errors})

@login_required(login_url='/login/')
def delete_opportunity(request, opportunity_id):
    opportunity = models.Opportunity.objects.get(id=opportunity_id)
    opportunity.delete()
    return redirect('/dashboard/opportunities/')

@login_required(login_url='/login/')
def alumni_view(request):
    alumni_list = models.Alumni.objects.all()
    current_user = request.user
    return render(request, 'admin/alumni_view.html', {'alumni_list': alumni_list, 'current_user': current_user})

@login_required(login_url='/login/')
def create_or_edit_alumni(request, alumni_id=None):
    current_user = request.user
    if alumni_id:
        alumni = models.Alumni.objects.get(id=alumni_id)
        if request.method == 'POST':
            form = forms.AlumniForm(request.POST, request.FILES, instance=alumni)
            if form.is_valid():
                alumni = form.save(commit=False)
                alumni.save()
                return redirect('/dashboard/alumni/')
        else:
            form = forms.AlumniForm(instance=alumni)
        return render(request, 'admin/alumni_dashboard.html', {'form': form, 'alumni': alumni, 'current_user': current_user, 'errors': form.errors})   
    else:
        if request.method == 'POST':
            form = forms.AlumniForm(request.POST, request.FILES)
            if form.is_valid():
                alumni = form.save(commit=False)
                alumni.save()
                return redirect('/dashboard/alumni/')
        else:
            form = forms.AlumniForm()

    return render(request, 'admin/alumni_dashboard.html', {'form': form, 'current_user': current_user, 'errors': form.errors})

@login_required(login_url='/login/')
def delete_alumni(request, alumni_id):
    alumni = models.Alumni.objects.get(id=alumni_id)
    alumni.delete()
    return redirect('/dashboard/alumni/')