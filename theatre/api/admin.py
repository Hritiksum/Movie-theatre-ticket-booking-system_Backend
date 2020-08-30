from django.contrib import admin

# Register your models here.

from .models import Customer,Movie_detail,Ticket_detail

admin.site.register(Customer)
admin.site.register(Movie_detail)
admin.site.register(Ticket_detail)
