from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer,MovieSerializer,TicketSerializer
from .models import Movie_detail
from datetime import datetime, timedelta

@api_view(['DELETE'])
def MovieRangeDelete(request):	
	time_threshold = datetime.now() + timedelta(hours=8)
	event=Movie_detail.objects.filter(movie_time__range=(datetime.now(),time_threshold))
	event.delete()
	#return Response("Item deleted")