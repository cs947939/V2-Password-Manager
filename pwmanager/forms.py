from pyexpat import model
from .models import PW
from django import forms

class PwEdit(forms.ModelForm):
    class Meta:
        model = PW
        fields = ["Username", "Password", "URL", "TOTP", "Notes"]

class Pwmake(forms.ModelForm):
    class Meta:
        model = PW
        fields = '__all__'