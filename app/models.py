from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(default="")

    def __str__(self):
        return self.username
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    ref_number = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.ref_number

class Customer(models.Model):
    name = models.CharField(max_length=100)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.name
    
class Member(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    
    def __str__(self):
        return self.fname