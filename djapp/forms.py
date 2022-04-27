from dataclasses import fields
from pyexpat import model
from socket import fromshare
from django import forms
from .models import Student,Track
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('fname','lname','age','student_track')
        widgets ={'fname':forms.TextInput(attrs={'placeholder':'Example. Mohammed','class':'form-control'}),
       
        'lname':forms.TextInput(attrs={'class':'form-control'}),
        
        'age':forms.NumberInput(attrs={'class':'form-control'}),
        'student_track':forms.Select(attrs={'class':'form-control'})
        
        
        }
   
class TrackForm(forms.ModelForm):
    class Meta:
        model=Track
        fields=('track_name',)