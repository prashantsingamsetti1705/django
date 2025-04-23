from django import forms
from django.core import validators
# def starts_with_s(value):
#     print('starts_with_s function execution')
#     if value[0].lower() != 's':
#         raise forms.ValidationError('Name should be starts with s or S')
class StudentForm(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()
    email=forms.EmailField()
    feed_back=forms.CharField(widget=forms.Textarea,validators=[
	validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    def clean_name(self):
        print("validting the name...")
        input_name=self.cleaned_data['name']
        if len(input_name) < 4:
            raise forms.ValidationError("mainimum number of the char it four")
        return input_name