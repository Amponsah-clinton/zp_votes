from django import forms

class InitialsLoginForm(forms.Form):
    initials = forms.CharField(
        max_length=10,
        label="Enter your initials",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. CA'
        })
    )

    password = forms.CharField(
        label="Enter your password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. zpec1234'
        })
    )
