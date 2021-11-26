from django.db import models
from Checkout.models import Project_Creation
# Create your models here.

class Offer_Details(models.Model):
    Project_Id = models.ForeignKey(Project_Creation, on_delete=models.CASCADE)
    Proof_Url = models.URLField()
    Proof_Url_Scnd = models.URLField(blank=True)
    Proof_Url_Third = models.URLField(blank=True)
    Messege = models.CharField(blank=True, max_length=500, default="N/A")

class Earned_by_Freelancer(models.Model):
    Money_Reciever = models.IntegerField()
    Money_Releser = models.IntegerField()
    Value = models.IntegerField(blank=True, default=0)
    Date_Created = models.DateField(auto_now_add=True)


