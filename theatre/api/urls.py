from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('ticketlist', views.TicketList, name="TicketList"),
    path('ticketorderlist', views.TicketOrderList, name="TicketOrderList"),
]
