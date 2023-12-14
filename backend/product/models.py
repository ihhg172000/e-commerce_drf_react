from django.db import models
from users.models import User



"""category table"""
class Category(models.Model):
	name = models.CharField(max_length=200, default="", blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return (self.name)



"""Brand table"""
class Brand(models.Model):
	name = models.CharField(max_length=200, default="", blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return (self.name)



"""product table"""
class Product(models.Model):
	name = models.CharField(max_length=200, default="", blank=False)
	description = models.TextField(max_length=1000, default="", blank=False)
	price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	quantity = models.IntegerField(default=0)
	#image = 
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)        # many to one 
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # many to one
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return (self.name)



	


