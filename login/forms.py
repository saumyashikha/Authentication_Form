from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control txt','placeholder':'Enter Password.....'}))
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput(attrs={'class':'form-control txt','placeholder':'Confirm Password.....'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': 'User_Name', 'first_name':'First_Name', 'last_name':'Last_name', 'email':'Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control txt','placeholder':'Enter Username.....'}),
            'first_name':forms.TextInput(attrs={'class':'form-control txt','placeholder':'Enter First name.....'}),
            'last_name':forms.TextInput(attrs={'class':'form-control txt','placeholder':'Enter Last name.....'}),
            'email':forms.EmailInput(attrs={'class':'form-control txt','placeholder':'Enter Email.....'})
        }

class LoginForm(AuthenticationForm):
        username = UsernameField(widget= forms.TextInput(attrs={'class':'form-control txt', 'placeholder':'Enter your Username.....'}))
        password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control txt', 'placeholder':'Enter Your Password.....'}))       