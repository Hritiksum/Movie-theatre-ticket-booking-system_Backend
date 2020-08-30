from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer,MovieSerializer,TicketSerializer

from .models import Customer,Movie_detail,Ticket_detail
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Movie':'/movie-list/',
		'Customer':'/customer-details/<str:name>/',
		'Buy':'/buy-tickets',#'Create':'/task-create/',
		'Update':'/ticket-update/<str:pk>/',
		'Delete':'/ticket-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def TicketList(request):
	Ticketlist = Movie_detail.objects.all().order_by('id')
	serializer = MovieSerializer(Ticketlist, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def TicketOrderList(request):
	Ticketorderlist = Ticket_detail.objects.all().order_by('id')
	serializer = TicketSerializer(Ticketorderlist, many=True)
	return Response(serializer.data)
