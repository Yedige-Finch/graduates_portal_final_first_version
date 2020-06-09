from django import forms
from django.forms import ModelForm
from .models import Student,Employer,User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field


# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ('student_id','course', 'speciality', 'phone')
    
#     def __init__(self, *args, **kwargs):
#     	super(StudentForm, self).__init__(*args, **kwargs)
#     	for field in self.fields.values():
#     		field.widget.attrs['class'] = 'form-control'
