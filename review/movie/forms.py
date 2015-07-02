from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={'size': '20'}))