from rest_framework import serializers
from .models import Customer,Movie_detail,Ticket_detail

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields ='__all__'

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie_detail
		fields ='__all__'

class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket_detail
		fields ='__all__'