from django.contrib import admin
from .models import Farmer, Saving, Loan, Notification, Transaction

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Saving)
admin.site.register(Loan)
admin.site.register(Notification)
admin.site.register(Transaction)
