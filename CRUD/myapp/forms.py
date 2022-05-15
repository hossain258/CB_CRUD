from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
        
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }