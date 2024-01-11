from django import forms
from adminpanel.models import MovieDetails,MovieTheaters

class MovieDetailsForm(forms.ModelForm):
    class Meta:
        model=MovieDetails
        fields='__all__'
        labels={
            'movie_name': '',
            'director': '',
            'description': '',
            'release_date': '',
            'banner_photo': 'Movie Poster',

        }
        widgets = {
            'movie_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie Name'}),
            'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Director'}),            
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Release Date','type':'date'}),
            'banner_photo': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control','type':'file'}),
             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),}


class movies_form(forms.ModelForm):
    class Meta:
        model = MovieTheaters
        fields = '__all__'
        labels = {
            'Theater': '',
            'Movie': '',

        }
        Widgets = {
            'Theater': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Theater Name'}),
            'Movie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie Name'}),
        }