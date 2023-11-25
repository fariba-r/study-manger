from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, required=True,label="Username")
    password = forms.CharField(max_length=10, required=True, label="Password")


    