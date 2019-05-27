from django.db import models
from django.core.files import File
import os

# Create your models here.
class Food(models.Model):
    reference = models.IntegerField(null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255,null=True)
    price = models.IntegerField(null=True)
    picture = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="foods"

class Contact(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    food = models.OneToOneField(Food, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE) #cascade delete the reservation done with contact
    def __str__(self):
        return self.contact.name

