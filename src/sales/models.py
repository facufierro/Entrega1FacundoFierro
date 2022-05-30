from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.name
