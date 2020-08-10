from django import forms
from django.contrib.auth.models import User
class create_user(forms.ModelForm):
    class Meta:
        model=User
        field=['username','password','email','firstname','lastname']
