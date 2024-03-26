from django.db import models

# Create your models here.
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
    Product_Price = models.IntegerField()
    Description = models.TextField()
    Location = models.TextField()
    Phone_Number = models.IntegerField()
    category = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='shop/images',default='')
    def __str__(self):
        return self.Product_Name