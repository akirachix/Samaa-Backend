from django.db import models
from django.utils import timezone
from farmer.models import Farmer


class Loan(models.Model):
    farmer_id_number = models.ForeignKey('farmer.Farmer', on_delete=models.CASCADE)  
    amount_requested = models.FloatField()
    amount_approved = models.FloatField()
    status = models.CharField(max_length=50)
    request_date = models.DateTimeField()
    approval_date = models.DateTimeField(null=True, blank=True)
    repayment_date = models.DateTimeField(null=True, blank=True)


    

    def __str__(self):
        return f'{self.status}'

