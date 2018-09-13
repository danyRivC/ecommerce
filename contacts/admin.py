from django.contrib import admin
from contacts.models import ContactModel
# Register your models here.

class ContactAdmin (admin.ModelAdmin):
    list_display=('title','message','email_contact')

admin.site.register(ContactModel, ContactAdmin)
