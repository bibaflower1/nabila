from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget = forms.TextInput(attrs={'class':'form-control'}),
     required=True)

    address = forms.CharField(label='Address', max_length=100, widget = forms.TextInput(attrs={'class':'form-control'}),
     required=True)