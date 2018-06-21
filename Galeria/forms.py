from .models import Usuario
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class UserForm(forms.ModelForm):
     class Meta:
         model = Usuario
         fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'password','telefono', 'last_login', 'date_joined']
         widgets = {
             'telefono' : PhoneNumberPrefixWidget(),
         }