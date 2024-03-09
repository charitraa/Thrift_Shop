from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=200,default='SOME STRING')
    phone_Number= models.CharField(max_length=200,default='SOME STRING')
    Gender = models.CharField(max_length=200,default='SOME STRING')
    Date_of_birth = models.DateField(null=True)
    Email = models.EmailField(default='SOME STRING')
    password = models.CharField(max_length=200 ,default='SOME STRING')
    
    def __str__(self):
        return self.Username