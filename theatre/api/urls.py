from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('avail-ticketlist/', views.AvailTicketList, name="AvailTicketList"),
    path('ordered-ticketlist/', views.TicketOrderedList, name="TicketOrderedList"),
    path('user-details/<str:pk>/', views.UserDetails, name="UserDetails"),
    path('buy-ticket/', views.BuyTicket, name="BuyTicket"),
    path('update-movie-timing/<str:pk>/', views.UpdateMovieTiming, name="UpdateMovieTiming"),
    path('delete-ticket/<str:Tid>/', views.DeleteTicket, name="DeleteTicket"),
    path('movie-details/<str:Mid>/', views.MovieDetails, name="MovieDetails"),
    path('movie-delete/<str:Mid>/', views.MovieDelete, name="MovieDelete"),
    path('movie-time/<str:mt>/', views.MovieTime, name="MovieTime"),
    path('movie-range-view/', views.MovieRangeView, name="MovieRangeView"),
    path('movie-range-delete/', views.MovieRangeDelete, name="MovieRangeDelete"),
]
