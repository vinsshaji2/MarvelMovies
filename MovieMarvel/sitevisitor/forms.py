from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from adminpanel.models import User, Customer,Theatre


class LoginForm(AuthenticationForm):
     # Define a custom widget for the password fields
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    class Meta:
        model = User
        fields =['username','password']     

class UserAuthenticationForm(UserCreationForm):
    # Define a custom widget for the password fields
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter password'})
    )
    class Meta:
        model = User
        fields =['first_name','last_name','email','username','password1','password2']
        labels = {
        'first_name': '',
        'last_name': '',
        'email': '',
        'username': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
             }

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields='__all__'
        exclude=['status','user']
        labels = {
        'phone': '',
        'address': '',
        'place': '',
        'state': '',
        'id_proof': '',
        'profile_photo': '',
        
        }
        
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'placeholder': 'Place', 'class': 'form-control'}),
            'profile_photo': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'id_proof': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
        }

class TheatreRegistrationForm(forms.ModelForm):
    class Meta:
        model= Theatre
        fields='__all__'
        exclude=['status','user']
        labels = {
        'phone': '',
        'address': '',
        'place': '',
        'state': '',
        'pancard': '',
        'license_number': '',
        
        
        }
        
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'placeholder': 'Place', 'class': 'form-control'}),
            'pancard': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'license_number': forms.TextInput(attrs={'placeholder': 'License Number', 'class': 'form-control'}),
        }
        