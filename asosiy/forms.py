from django import forms
from django.core.exceptions import ValidationError
from .models import *

class StudentForm(forms.Form):
    i=forms.CharField(label= "Ism")
    j=forms.CharField(label="Jins")
    bitiruvchi=forms.BooleanField()
    kitoblari_soni=forms.IntegerField()

    def clean_i(self):
        qiymat=self.cleaned_data.get('i')
        if not qiymat.endswith('jon') and not qiymat.endswith('bek'):
            raise ValidationError("Ism o'zbekcha emas!")
        return qiymat
    def clean_kitoblari_soni(self):
        son=self.cleaned_data.get('kitoblari_soni')
        if son<0 or son>5:
            raise ValidationError("Kitoblar meyori cheklangan!")
        return son

class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields=('nom','sahifa','janr','muallif')
