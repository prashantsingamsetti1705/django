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
    password=forms.CharField(label='password',widget=forms.PasswordInput)
    rpassword=forms.CharField(label="againpassword",widget=forms.PasswordInput)
    feed_back=forms.CharField(widget=forms.Textarea,validators=[
	validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    # def clean(self):
    #     print('Total Form Validations......')
    #     total_cleaned_data = super().clean()
    #     print('Validating Name')
    #     input_name = total_cleaned_data['name']
    #     if input_name[0].lower() != 's':
    #         raise forms.ValidationError('Name should be starts with s')
    #     print('Validating Rollno')
    #     input_marks = total_cleaned_data['marks']
    #     if input_marks <= 0:
    #         raise forms.ValidationError('Rollno should be > 0')
    #     print('Validating Email')
    #     input_email = total_cleaned_data['email']
    #     if not input_email.endswith("@gmail.com"):
    #         raise forms.ValidationError('Email extension should be gmail')
    def clean(self):
        total_cleaned_data=super().clean()
        print("password valiadting")
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['rpassword']
        if pwd!=rpwd:
            raise forms.ValidationError("pwd and rpwd should be equal")