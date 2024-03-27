from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
def validate_image_width(value):
    width = value.width
    if width!=400:
        raise ValidationError('Image width must be 400 pixels.')
class Customer(models.Model):
    Username = models.CharField(max_length=200,default='')
    phone_Number= models.CharField(max_length=200,default='')
    Gender = models.CharField(max_length=200,default='')
    Date_of_birth = models.DateField(null=True)
    Email = models.EmailField(default='')
    password = models.CharField(max_length=200 ,default='')
    
    def __str__(self):
        return self.Username

class Product(models.Model):
    Product_Name = models.CharField(max_length=200)
    Product_pub = models.DateField(default=timezone.now)
    Product_Price = models.CharField(max_length=200)
    Description = models.TextField()
    Location = models.CharField(max_length=200)
    Phone_Number = models.CharField(max_length=200,default='')
    category = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='images',default='')
    def __str__(self):
        return self.Product_Name