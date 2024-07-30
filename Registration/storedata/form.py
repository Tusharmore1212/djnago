from django import forms


class UserForms(forms.Form):
    Email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))