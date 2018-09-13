from django.shortcuts import render
from contacts.forms import ContactForm
from contacts.models import ContactModel
def contacts(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            title = data['title']
            message = data['description']
            email_contact= data['email_contact']
            phone_number = data['phone_number']
            contact = ContactModel(title=title,
                                   message=message,
                                   email_contact= email_contact,
                                   phone_number=phone_number,
                                   )
            contact.save()



    return render(request,'contacts/contacts.html')
