from django import forms
from . import models

class AchievementForm(forms.ModelForm):
    class Meta:
        model = models.Achievement
        fields = ['title', 'description', 'date_achieved', 'image', 'category']