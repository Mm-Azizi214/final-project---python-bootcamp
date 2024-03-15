from django import forms
from final.models import Criticism

class Criticism_Form(forms.Form) :
    moive_name= forms.CharField()
    body=forms.CharField()
    created=forms.DateTimeField()

class Criticism_update_Form(forms.ModelForm) :
    class Meta :
        model=Criticism
        fields=("moive_name","body","created")

