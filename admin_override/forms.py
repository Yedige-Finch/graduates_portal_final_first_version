from django import forms
from django.forms import ModelForm
from .models import Feedback
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ('date',)
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'