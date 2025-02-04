from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta

class NewsPage(models.Model):
    CATEGORY_CHOICES = [
        ('Event', 'Event'),
        ('Achievement', 'Achievement'),
        ('General', 'General'),
    ]

    title = models.CharField(max_length=255, unique=True)  
    content = models.TextField()  
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    published_date = models.DateTimeField(default=now)  
    image = models.ImageField(upload_to='static/images/news_images/', blank=True, null=True)  
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='General')  
    is_published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)  

    class Meta:
        ordering = ['-published_date']  

    def __str__(self):
        return self.title

class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('Academics', 'Academics'),
        ('Sports', 'Sports'),
        ('Research', 'Research'),
        ('Entrepreneurship', 'Entrepreneurship'),
        ('Others', 'Others'),
    ]

    title = models.CharField(max_length=255, unique=True)  
    description = models.TextField()  
    date_achieved = models.DateField(default=now)  
    image = models.ImageField(upload_to='static/images/achievements/', blank=True, null=True)  
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Others')  
    is_approved = models.BooleanField(default=True)  

    class Meta:
        ordering = ['-date_achieved']  

    def __str__(self):
        return self.title

    def is_present(self):
        """Return True if the achievement is less than a year old, False otherwise."""
        return self.date_achieved >= now().date() - timedelta(days=365)

class Alumni(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics & Communication'),
        ('EEE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('CHE', 'Chemical Engineering'),
        ('MME', 'Metallurgical & Materials Engineering'),
        ('Others', 'Others'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)  
    graduation_year = models.IntegerField()  
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    domain = models.CharField(max_length=255, blank=True, null=True)  # Field for domain (e.g., Software Development)
    current_position = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    
    # Location stored as JSON (latitude, longitude, and address)
    location = models.JSONField(blank=True, null=True, default=dict)

    # List of skills (stored as JSON)
    skills = models.JSONField(blank=True, null=True, default=list)

    # Achievements stored as JSON (title, description, year)
    achievements = models.JSONField(blank=True, null=True, default=list)

    # Social Media Links
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    # Profile Picture
    profile_picture = models.ImageField(upload_to='static/images/alumni/', blank=True, null=True)  # Using URL instead of ImageField

    class Meta:
        ordering = ['-graduation_year', 'name']

    def __str__(self):
        return f"{self.name} ({self.graduation_year})"

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Conference', 'Conference'),
        ('Workshop', 'Workshop'),
        ('Seminar', 'Seminar'),
        ('Meetup', 'Meetup'),
        ('Others', 'Others'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    image = models.ImageField(upload_to='static/images/events/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Others')

    class Meta:
        ordering = ['start_date', 'title']

    def __str__(self):
        return self.title

    def is_past(self):
        """Returns True if the event is in the past."""
        return self.start_date < now()

    def is_upcoming(self):
        """Returns True if the event is upcoming (today or in the future)."""
        return self.start_date >= now()

class Opportunity(models.Model):
    OPPORTUNITY_TYPES = [
        ('Job', 'Job'),
        ('Internship', 'Internship'),
        ('Scholarship', 'Scholarship'),
        ('Fellowship', 'Fellowship'),
        ('Research', 'Research'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=100, choices=[
        ('Remote', 'Remote'),
        ('On-Site', 'On-Site'),
        ('Hybrid', 'Hybrid')
    ], default='On-Site')
    opportunity_type = models.CharField(max_length=50, choices=OPPORTUNITY_TYPES, default='Job')
    image = models.ImageField(upload_to='static/images/opportunities/', blank=True, null=True)
    description = models.TextField()
    application_link = models.URLField(blank=True, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
