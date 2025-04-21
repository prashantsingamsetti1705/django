from django import forms
class StudentFrom(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()
    email=forms.EmailField()
    feed_back=forms.CharField(widget=forms.Textarea)