from django import forms
from django.forms import ModelForm
from review.movie.models import Review

RANKINGS = (
        (0,'0'),
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
    )

class SearchForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={'size': '20'}))


class ReviewForm(ModelForm):
    #movie = forms.CharField(widget=forms.HiddenInput())

    funny = forms.IntegerField(widget=forms.Select(attrs={'class': "cat1"}, choices=RANKINGS),)
    action = forms.IntegerField(widget=forms.Select(attrs={'class': "cat2"}, choices=RANKINGS),)
    adventure = forms.IntegerField(widget=forms.Select(attrs={'class': "cat3"}, choices=RANKINGS),)
    scare = forms.IntegerField(widget=forms.Select(attrs={'class': "cat4"}, choices=RANKINGS),)
    romance = forms.IntegerField(widget=forms.Select(attrs={'class': "cat5"}, choices=RANKINGS),)
    sad = forms.IntegerField(widget=forms.Select(attrs={'class': "cat6"}, choices=RANKINGS),)
    sexual = forms.IntegerField(widget=forms.Select(attrs={'class': "cat7"}, choices=RANKINGS),)
    alcohol_drug = forms.IntegerField(widget=forms.Select(attrs={'class': "cat8"}, choices=RANKINGS),)
    violence = forms.IntegerField(widget=forms.Select(attrs={'class': "cat9"}, choices=RANKINGS),)
    gore = forms.IntegerField(widget=forms.Select(attrs={'class': "cat10"}, choices=RANKINGS),)
    bad_language = forms.IntegerField(widget=forms.Select(attrs={'class': "cat11"}, choices=RANKINGS),)
    intelectual = forms.IntegerField(widget=forms.Select(attrs={'class': "cat12"}, choices=RANKINGS),)
    kid_friendly = forms.IntegerField(widget=forms.Select(attrs={'class': "cat13"}, choices=RANKINGS),)
    overall = forms.IntegerField(widget=forms.Select(attrs={'class': "cat14"}, choices=RANKINGS),)

    class Meta:
        model = Review
        exclude= []