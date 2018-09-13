from django import forms
class ContactForm(forms.Form):


    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(max_length=600, required=True)
    phone_number = forms.CharField(max_length=20,required=True)
    email_contact = forms.CharField(max_length=200,required=True)
