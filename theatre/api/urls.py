from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('availticketlist', views.AvailTicketList, name="AvailTicketList"),
    path('ticketorderlist', views.TicketOrderList, name="TicketOrderList"),
    path('userdetails/<str:pk>/', views.UserDetails, name="UserDetails"),
    path('buyticket', views.BuyTicket, name="BuyTicket"),
]
