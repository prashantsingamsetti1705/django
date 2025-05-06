from django import forms
class Additems_from(forms.Form):
    itemname=forms.CharField()
    quantity=forms.IntegerField()