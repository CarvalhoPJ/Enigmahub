from django import forms
from django.forms import ModelForm
from .models import Enigma


class EnigmaForm(forms.ModelForm):
    class Meta:
        model =Enigma
        fields =['title','description','correct_answer','tips']


class AnswerForm(forms.ModelForm):
    answer =forms.CharField(label='Answer', max_length=100)
