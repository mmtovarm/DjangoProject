from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'image', 'pub_date', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                format='%m/%d/%y',
                attrs={
                    'class':'formm-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            )
        }

