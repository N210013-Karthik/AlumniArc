from django.contrib import admin
from .models import NewsPage, Achievement, Alumni

# Register your models here.

admin.site.register(NewsPage)
admin.site.register(Achievement)
admin.site.register(Alumni)