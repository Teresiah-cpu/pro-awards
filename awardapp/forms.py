from django import forms
from .models import Profile,Project, Review

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','project']

class AddProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['user']

class AddReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['design_rating','usability_rating', 'content_rating', 'comment']