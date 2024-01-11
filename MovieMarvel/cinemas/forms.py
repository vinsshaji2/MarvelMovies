from django import forms
from adminpanel.models import  ScreenDetails,SlotDetails,ShowDetails,TicketDetails,MovieDetails


class ScreenDetailsForm(forms.ModelForm):
    class Meta:
        model=ScreenDetails
        fields='__all__'
        exclude=['theatre']
        labels={
            'screen_name': '',
            'seat_count': '',
             
        }
        widgets = {
            'screen_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Screen Name'}),
            'seat_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Seat Count'}),   
        }         
class SlotDetailsForm(forms.ModelForm):
    class Meta:
        model = SlotDetails
        fields = '__all__'
        exclude=['ticket']
        labels={
            'row':'',
            'seat_number':'',

        }
        widgets = {
            'row': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'row'}),
            'seat_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Seat number'}),

        }



class ShowDetailsForm(forms.ModelForm):
    class Meta:
        model = ShowDetails
        fields = ['show_timing', 'movie']  # Define the fields to include in the form

    def __init__(self, *args, **kwargs):
        super(ShowDetailsForm, self).__init__(*args, **kwargs)
        # Customize the movie field to be a dropdown menu
        self.fields['movie'].widget = forms.Select(attrs={'class': 'form-control'})  # Customize the appearance if needed
        self.fields['movie'].queryset = MovieDetails.objects.all()
class TicketDetailsForm(forms.ModelForm):
    class Meta:
        model = TicketDetails
        fields = ['ticket_type', 'rate']  # Assuming you only want these fields for booking

    def __init__(self, *args, **kwargs):
        super(TicketDetailsForm, self).__init__(*args, **kwargs)