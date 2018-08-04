from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('restaurant','vegetarianUp','wasteUp','waterUp','localUp','comment')
