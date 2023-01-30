from django.db import models

# Create your models here.
class Table1(models.Model):

    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    place=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)




class Image(models.Model):

    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    place=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)