from django import forms
from .models import Books
from django.forms import ModelForm


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['name','author',]