from testapp.models import Student
from django import forms
class StudentForm(forms.ModelForm):
    name=forms.CharField()
    mark=forms.IntegerField()
    class Meta:
        model=Student
        fields='__all__'
        