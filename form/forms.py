from django.forms import ModelForm
from django import forms

from .models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('student_name', 'roll_no', 'subject', 'suggestion')
        widgets = {
            'student_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Student Name", 'title': "Enter Student Name",
                       'required': "True"}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Roll No", 'pattern': "[0-9]{10}",
                                              'title': "Enter Roll No.", 'required': "True"}),
            'subject': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Subject", 'title': "Enter Suggestion Subject",
                       'required': "True"}),
            'suggestion': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "Enter Suggestion Or Query .....................", 'title': "Input Suggestion",
                       'required': "True", 'style': "resize: none;height: 200px;"})
        }
