from django.db import models

from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Movie_detail(models.Model):
    movie_name=models.CharField(max_length=100, blank=False, unique=True)
    movie_time=models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    
    def __str__(self):
        return "%s (Time:-%s)" % (self.movie_name, self.movie_time)


class Ticket_detail(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    movie_detail=models.ForeignKey(Movie_detail,on_delete=models.CASCADE)
    tickets_quantity=models.IntegerField(default=1, validators=[MaxValueValidator(20), MinValueValidator(1)])

    def __str__(self):
        return "%s {%s} (%s)" % (self.customer.name,self.movie_detail.movie_name , self.tickets_quantity)
