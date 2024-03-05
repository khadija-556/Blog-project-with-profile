from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class customUserForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Username'}))
    email = forms.EmailField(widget= forms.EmailInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Username'}))
    password1 = forms.CharField(label='Password',widget= forms.PasswordInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Password'}))
    password2 = forms.CharField(label='Confirm Password',widget= forms.PasswordInput(
        attrs={'class' : 'form-control',
               'placeholder': 'Input Password'}))

    class Meta:
        model=Custom_user
        fields=fields = ['username','email','password1','password2','user_type','city']
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget= forms.TextInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your name'
        }
    ))
 
    password=forms.CharField(widget= forms.PasswordInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your password'
        }
    ))
    class Meta:
        model=Custom_user
        fields=['username','passwoard']
        

class blogForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields=('__all__')

class writterModelForm(forms.ModelForm):
    class Meta:
        model=writterProfile
        fields=('__all__')
        exclude = ['recent_blog','user']

class ReaderModelForm(forms.ModelForm):
    class Meta:
        model=ReaderProfile
        fields=('__all__')
        exclude = ['recent_blog','user']



        