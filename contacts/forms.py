from django import forms
from contacts.models import ContactModel
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields=('title','message','phone_number','email_contact')
