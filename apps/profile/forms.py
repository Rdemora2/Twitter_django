from django import forms

from .models import profile

class profile(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('avatar',)