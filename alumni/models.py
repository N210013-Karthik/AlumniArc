from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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
