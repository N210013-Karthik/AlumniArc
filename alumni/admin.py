from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.NewsPage)
admin.site.register(models.Achievement)
admin.site.register(models.Alumni)
admin.site.register(models.Event)