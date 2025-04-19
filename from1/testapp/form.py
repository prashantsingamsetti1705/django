from django import forms
class StudentFrom(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()