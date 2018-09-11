from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """docstring for Profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank= True)
    picture = models.ImageField(upload_to='accounts/pictures',
                                blank= True,
                                null = True)
    
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
