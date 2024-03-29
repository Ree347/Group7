from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Customer, Seller, Refund


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class SellerRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    sellerid=forms.CharField(label='Seller Id', widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'sellerid']


class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MyPasswordResetForm(PasswordChangeForm):
    pass


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'zipcode']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality':forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }

       
class SellerProfileForm(forms.ModelForm):
    
    model = Seller
    fields = ['name', 'locality', 'city', 'mobile', 'zipcode']
    widgets={
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'locality':forms.TextInput(attrs={'class': 'form-control'}),
        'city': forms.TextInput(attrs={'class': 'form-control'}),
        'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
        'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
    }



class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()
