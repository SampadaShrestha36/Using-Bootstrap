from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contactno=PhoneNumberField(blank=True, region='NP')
    message=models.TextField()

    def __str__(self):
        return self.name
    