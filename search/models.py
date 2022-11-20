'''
- https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#usage
- https://docs.djangoproject.com/en/4.1/topics/files/
- https://codepen.io/cristinaconacel/pen/OBKBPK
'''

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Restaurant(models.Model):
    name = models.TextField(max_length=255, blank=False, null=False)
    address = models.TextField(max_length=500, blank=False, null=False)
    phone = PhoneNumberField(blank=False)

    def __str__(self) -> str:
        return self.name


class FoodItem(models.Model):
    name =  models.TextField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=255, blank=False, null=False)
    image_link = models.TextField(blank=False, null=False)
    restaurant_id = models.ForeignKey("search.Restaurant", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
