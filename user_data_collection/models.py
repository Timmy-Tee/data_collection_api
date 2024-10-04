from django.db import models


# Create your models here.
class CustomerDetail(models.Model):
     STATUS_CHOICE = [
          ('Done', 'Done'),
          ('Not Done', 'Not Done'),
     ]
     
     customer_name = models.CharField(max_length=255)
     location = models.CharField(max_length=255)
     amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
     volume_dispensed = models.PositiveBigIntegerField()
     status = models.CharField(max_length=15,choices=STATUS_CHOICE)
     
     def __str__(self):
          return f'{self.customer_name}, {self.location}'