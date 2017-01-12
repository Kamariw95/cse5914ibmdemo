from django import forms

class PostForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)
