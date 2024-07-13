from django.db import models
from django.utils import timezone
from farmer.models import Farmer

class Transaction(models.Model):
    farmer_id_number = models.ForeignKey('farmer.Farmer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f' {self.amount}' 
