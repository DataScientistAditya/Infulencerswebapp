from django.db import models

# Create your models here.
class Advertisement_Create(models.Model):
    User = models.IntegerField()
    Product_Name = models.CharField(max_length=200)
    Product_Cost = models.IntegerField()
    Product_Description = models.CharField(max_length=1800)
    Category = models.CharField(max_length=20)
    Subcategories = models.CharField(max_length=50)
    Audience = models.CharField(max_length=20)
    Social_Media_Wanted = models.CharField(max_length=30)
    Influencer_Lavel = models.CharField(max_length=30)
    Target_Country = models.CharField(max_length=100)
    Product_image = models.ImageField(upload_to='Product_Image/')
    Is_Shipping = models.BooleanField(default=False)
    Date_Created = models.DateTimeField(auto_now_add=True)
