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
#movie avail list
def AvailTicketList(request):
	try:
		Ticketlist = Movie_detail.objects.all().order_by('id')
		serializer = MovieSerializer(Ticketlist, many=True)
		return Response(serializer.data)
	except:
		return Response(None)


@api_view(['GET'])
#tickes sold list
def TicketOrderedList(request):
	try:
		Ticketorderlist = Ticket_detail.objects.all().order_by('id')
		serializer = TicketSerializer(Ticketorderlist, many=True)
		return Response(serializer.data)
	except:
		return Response(None)


@api_view(['GET'])
#users details by Ticket ID
def UserDetails(request, pk):
	try:
		Ticketid = Ticket_detail.objects.get(id=pk)
		user = Ticketid.customer
		serializer = CustomerSerializer(user, many=False)
		return Response(serializer.data)
	except:
		return Response(None)

@api_view(['GET'])
#Movie details by movie ID
def MovieDetails(request, Mid):
	try:
		movie = Movie_detail.objects.get(id=Mid)
		serializer = MovieSerializer(movie, many=False)
		return Response(serializer.data)
	except:
		return Response(None)

@api_view(['POST'])
#Buy Movie Tickets
def BuyTicket(request):
	try:
		serializer = TicketSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)
	except:
		return Response(None)

@api_view(['POST'])
#Update Movie timing by movie id
def UpdateMovieTiming(request, pk):
	try:
		movie = Movie_detail.objects.get(id=pk)
		serializer = MovieSerializer(instance=movie, data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)
	except:
		return Response(None)


@api_view(['DELETE'])
#Delete movie tickets by Movie id
def DeleteTicket(request, Tid):
	try:
		movie = Movie_detail.objects.get(id=Tid)
		movie.delete()

		return Response('Ticket/Movie succsesfully deleted!')
	except:
		return Response(None)


@api_view(['GET'])
#Movie details by movie ID
def MovieDelete(request, Mid):
	try:
		movie = Movie_detail.objects.get(id=Mid)
		serializer = MovieSerializer(movie, many=False)
		return Response(serializer.data)
	except:
		return Response(None)


@api_view(['GET'])
#Movie details by movie ID
def MovieTime(request, mt):
	try:
		movie = Movie_detail.objects.filter(movie_time=mt)
		serializer = MovieSerializer(movie, many=True)
		return Response(serializer.data)
	except:
		return Response(None)


#@api_view(['GET'])
@api_view(['DELETE'])
def MovieRangeDelete(request):
	from datetime import datetime, timedelta
	time_threshold = datetime.now() + timedelta(hours=8)
	event=Movie_detail.objects.filter(movie_time__range=(datetime.now(),time_threshold))
	#serializer = MovieSerializer(event, many=True)
	event.delete()
	return Response("Item deleted")


@api_view(['GET'])
def MovieRangeView(request):
	from datetime import datetime, timedelta
	time_threshold = datetime.now() + timedelta(hours=8)
	event=Movie_detail.objects.filter(movie_time__range=(datetime.now(),time_threshold))
	serializer = MovieSerializer(event, many=True)
	return Response(serializer.data)