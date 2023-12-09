from django.db import models
from users.models import User
"""category table"""
class category(models.TextChoices):
	Mobiles = "Mobiles"
	Accessories = "Accessories"


"""product table"""
class Product(models.Model):
	name = models.CharField(max_length=200, default="", blank=False)
	description = models.TextField(max_length=1000, default="", blank=False)
	price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	quantity = models.IntegerField(default=0)
	#brand_id = 
	#category_id = 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)



	


