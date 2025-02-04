from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_header = "Alumni Portal Admin"
admin.site.site_title = "Alumni Admin"
admin.site.index_title = "Welcome to the Alumni Management System"

admin.site.register(models.NewsPage)
admin.site.register(models.Achievement)
admin.site.register(models.Alumni)
admin.site.register(models.Event)