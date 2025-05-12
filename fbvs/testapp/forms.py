from django import forms
from testapp.models import Emplooye
class Employeefrom(forms.ModelForm):
    class Meta:
        model=Emplooye
        fields='__all__'
