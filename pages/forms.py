from django.forms import ModelForm, TextInput, Textarea, NumberInput
from django.views.generic import FormView

from pages.models import Page


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': TextInput(attrs={'class': "form-control", 'placeholder': "Título"}),
            'content': Textarea(attrs={'class': "form-control"}),
            'order': NumberInput(attrs={'class': "form-control"}),
        }
        labels = {
            'title': '', 'content': '', 'order': ''
        }
