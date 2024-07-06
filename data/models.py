from django.db import models
from django.utils import timezone

class Farmer(models.Model):
    farmers_id = models.AutoField(primary_key=True)
    farmerName = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    full_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class Saving(models.Model):
    savings_id = models.AutoField(primary_key=True)
    farmers_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    saving_date = models.DateTimeField(default=timezone.now)

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    farmers_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    amount_requested = models.FloatField()
    amount_approved = models.FloatField()
    status = models.CharField(max_length=50)
    request_date = models.DateTimeField()
    approval_date = models.DateTimeField(null=True, blank=True)
    repayment_date = models.DateTimeField(null=True, blank=True)

class Notification(models.Model):
    notifications_id = models.AutoField(primary_key=True)
    farmers_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    message = models.TextField()
    type = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    farmers_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
