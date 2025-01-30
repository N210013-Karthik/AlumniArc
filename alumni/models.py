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
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  
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
    achiever = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    date_achieved = models.DateField(default=now)  
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)  
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Others')  
    is_approved = models.BooleanField(default=True)  

    class Meta:
        ordering = ['-date_achieved']  

    def __str__(self):
        return self.title

    def is_present(self):
        """Return True if the achievement is less than a year old, False otherwise."""
        return self.date_achieved >= now().date() - timedelta(days=365)

from django.db import models

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
    phone = models.CharField(max_length=15, blank=True, null=True)  
    batch = models.IntegerField()  
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)  
    current_position = models.CharField(max_length=255, blank=True, null=True)  
    company = models.CharField(max_length=255, blank=True, null=True)  
    location = models.CharField(max_length=255, blank=True, null=True)  
    linkedin = models.URLField(blank=True, null=True)  
    twitter = models.URLField(blank=True, null=True)  
    profile_picture = models.ImageField(upload_to='alumni_photos/', blank=True, null=True)  

    class Meta:
        ordering = ['-batch', 'name']  

    def __str__(self):
        return f"{self.name} ({self.batch})"
