
from django import forms
from django.core import validators
from django.contrib.auth.models import User



class RegistrationForm(forms.Form):
    
      
        
    username = forms.RegexField(regex=r'^\w+$', max_length=30,widget=forms.TextInput())
    email = forms.EmailField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
           
    
    def isValidUsername(self, field_data, all_data):
        try:
            User.objects.get(username=field_data)
        except User.DoesNotExist:
            return
        raise validators.ValidationError('The username "%s" is already taken.' % field_data)
    
    def save(self, new_data):
        u = User.objects.create_user(new_data['username'],new_data['email'],new_data['password1'])
        u.is_active = False
        u.save()
        return u

