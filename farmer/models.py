from django.db import models


class Farmer(models.Model):
    farmer_id_number = models.CharField(max_length=20, unique=True, primary_key=True)
    email = models.EmailField(unique=True) 
    password_hash = models.CharField(max_length=255)
    full_name = models.CharField(max_length=25, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)



    def __str__(self):
        return f'{self.full_name}'