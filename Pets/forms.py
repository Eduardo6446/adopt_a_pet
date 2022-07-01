from pyexpat import model
from django import forms
from .models import *


class formApregarMascota(forms.ModelForm):
    class Meta:
       model = Pet

       fields = [
        'name',
        'breed',
        'species',
        'age',
        'description',
        'pet_pic'
       ]