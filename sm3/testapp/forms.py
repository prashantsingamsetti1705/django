from django  import forms
class Name_form(forms.Form):
    name=forms.CharField()
#now for the age 
class Age_form(forms.Form):
    age=forms.IntegerField()
#now gilrs friend name
class Gf_form(forms.Form):
    name=forms.CharField()