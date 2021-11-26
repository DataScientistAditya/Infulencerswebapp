from django.db import models
from Checkout.models import Project_Creation

# Create your models here.


class AmountChange(models.Model):
    Project_Id = models.ForeignKey(Project_Creation,on_delete=models.CASCADE)
    Change_Amount = models.IntegerField()
    Meesege = models.CharField(max_length=500, blank=True)
    is_Approved = models.BooleanField(default=False)
