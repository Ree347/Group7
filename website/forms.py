from django import forms
from .models import Member


#define table 

class MemberForm(forms.ModelForm):
    class Meta:
        model= Member
        fields = ['fname', 'lname', 'email', 'passwd', 'age']