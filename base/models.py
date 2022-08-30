from itertools import product
from unicodedata import category
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
# Create your models here.

class Products(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True) 
    name = models.CharField(max_length=150, null= True, blank=True)
    image = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=150, null= True, blank=True)
    category =models.CharField(max_length=150, null= True, blank=True)
    description =models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    countInStock = models.IntegerField(null= True, blank= True, default=0)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    product= models.ForeignKey(Products, on_delete = models.SET_NULL, null=True) 
    user= models.ForeignKey(User, on_delete = models.SET_NULL, null=True) 
    name= models.CharField(max_length=150, null= True, blank=True)
    rating= models.IntegerField(null=True, blank=True, default=0)
    comment= models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.rating)

class Order(models.Model): 
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True) 
    paymentMethod = models.CharField(max_length=150, null= True, blank=True)
    taxPrice = models.DecimalField(max_digits=5, decimal_places=2)
    shippingPrice = models.DecimalField(max_digits=5, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=5, decimal_places=2)
    isPaid = models.BooleanField(default= False)
    paidAt = models.DateField(auto_now_add=True)
    isDelivered = models.BooleanField(default= False)
    deliveredAt = models.DateField(auto_now_add=True)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.createdAt)


class OrderItem(models.Model): 
    product = models.ForeignKey(Products, on_delete = models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=150, null= True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)

