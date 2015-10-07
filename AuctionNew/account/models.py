from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
#from products.models import *


# Create your models here.
class Address(models.Model):
	Street_address = models.CharField(null=True,blank=True,max_length=98)
	City = models.CharField(null=True,blank=True,max_length=98)
	State = models.CharField(null=True,blank=True,max_length=98)
	Pincode = models.IntegerField(null=True,blank=True,max_length=6)

class MyUser(AbstractUser):
    Dob = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(unique = True, null=True,help_text=('Only Indian'), max_length = 13)
    Address = models.ForeignKey(Address, null = True)

#class InterestedIn(models.Model):
#	By = models.ForeignKey(MyUser)
#	items = models.ManyToManyField(Product)


