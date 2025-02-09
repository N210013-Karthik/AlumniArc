from django import forms
from . import models

class AchievementForm(forms.ModelForm):
    class Meta:
        model = models.Achievement
        fields = ['title', 'description', 'date_achieved', 'image', 'category']
        
class OpportunityForm(forms.ModelForm):
    class Meta:
        model = models.Opportunity
        fields = ['title', 'company', 'location', 'opportunity_type', 'image', 'description', 'application_link', 'deadline']
        
class AlumniForm(forms.ModelForm):
    class Meta:
        model = models.Alumni
        fields = ['name', 'email', 'mobile', 'graduation_year', 'department', 'domain', 'current_position', 'company', 'location', 'skills', 'achievements', 'linkedin', 'twitter', 'profile_picture']
        
class NewsForm(forms.ModelForm):
    class Meta:
        model = models.NewsPage
        fields = ['title', 'content', 'image', 'category']