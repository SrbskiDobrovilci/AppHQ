
from django.db import models

class Products(models.Model):
    minUser = models.IntegerField()
    maxUser = models.IntegerField()
    creator = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    date = models.DateField()
    startTime = models.TimeField()
    price  = models.DecimalField(max_digits = 8, decimal_places = 2)

class Groups(models.Model):
    name = models.CharField(max_length = 255)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
        

class Lessons(models.Model):
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    link = models.URLField(max_length = 255)
    
    
class Students(models.Model):
    name = models.CharField( max_length=50)
    groupId = models.ForeignKey(Groups, on_delete=models.CASCADE) 

class Accesses(models.Model):
    userId = models.ForeignKey(Students, on_delete=models.CASCADE)
    productId = models.ForeignKey(Products, on_delete=models.CASCADE)
