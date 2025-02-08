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