from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your models here.
class ContactModel(models.Model):
    client = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=600)
    created_at=models.DateTimeField(auto_now_add=True)
    email_contact = models.CharField(max_length=200)
