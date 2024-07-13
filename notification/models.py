from django.db import models
from django.utils import timezone
from farmer.models import Farmer

class Notification(models.Model):
    farmer_id_number = models.ForeignKey('farmer.Farmer', on_delete=models.CASCADE)  
    message = models.TextField()
    type = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.message}'  
