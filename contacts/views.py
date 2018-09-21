from django.shortcuts import render, redirect
from contacts.forms import ContactForm
from products.models import Product

def contacts(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success='Pregunta enviada, Ponto te responderemos'
            products = Product.objects.all()
            

    return render(request=request,
                  template_name='contacts/contacts.html')
