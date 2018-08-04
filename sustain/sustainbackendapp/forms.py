from django import forms
from .models import Review

class ReviewForm(forms.Form):
    class Meta:
        model = Review
        fields = ('restaurant')
