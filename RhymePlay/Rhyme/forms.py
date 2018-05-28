from django.forms import forms
from django import forms


class Rhyme(forms.Form):
    """ Sign Up """
    rhyme = forms.CharField(max_length =255,widget=forms.TextInput(attrs={"placeholder":"Rhyme!"}))
    