from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('availticketlist', views.AvailTicketList, name="AvailTicketList"),
    path('ticketorderlist', views.TicketOrderList, name="TicketOrderList"),
    path('userdetails/<str:pk>/', views.UserDetails, name="UserDetails"),
    path('buyticket', views.BuyTicket, name="BuyTicket"),
    path('updatemovietiming/<str:pk>/', views.UpdateMovieTiming, name="UpdateMovieTiming"),
    path('deleteticket/<str:Tid>/', views.DeleteTicket, name="DeleteTicket"),
    path('moviedetails/<str:Mid>/', views.MovieDetails, name="MovieDetails"),
    path('moviedelete/<str:Mid>/', views.MovieDelete, name="MovieDelete"),
    path('movietime/<str:mt>/', views.MovieTime, name="MovieTime"),
]
