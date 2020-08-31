# Movie-theatre-ticket-booking-system_Backend
 
 **TECH STACK**
 Python, Django(Framework), SQLite database
 
 ## SQLite database
 ***************************
 ![automated testing](sql.png)
 ● Customer table     (ID,Name,phone number,time)
 ● Movie table        (ID,Movie name,Movie time)
 ● Ticket Order table (ID,Customer key,Movie key,No. of tickets ordered)
 
 
 ## Rest API Overview
 ***************************
 ![automated testing](apioverview.png)
 http://127.0.0.1:8000/api/
 ● Contain the list of all rest api created
 
 
 
 ## Show all Avail Movies list
 ***************************
![automated testing](availmovieslist.png)
http://127.0.0.1:8000/api/avail-ticketlist/
● Api will show the list of all the movie available to buy.

## POST REST API to Buy tickets
***************************
![automated testing](buytickets.png)
http://127.0.0.1:8000/api/buy-ticket/
● Post api to buy tickets not more than 20 tickets.
● POST request format:
{
        "tickets_quantity": 5,
        "customer": 1,
        "movie_detail": 1
}
● Ask for customer id,movie id and number of tickets wants to buy.
● Ticket order id will be automatically updated.
● Ticket quantity can't be more than 20 (validation)

## POST REST API Delete Ticket
***************************
![automated testing](moviedeletebymovieid.png)
http://127.0.0.1:8000/api/movie-delete/<str:Mid>/
● Post api ask for movie id to detele is from database.


## GET REST API to get buyed Movie details by ordered ticket ID
***************************
![automated testing](moviedetailbymovieid.png)
http://127.0.0.1:8000/api/movie-details/<str:Mid>/
● Post api to get details of movie from ordered ticket's ID

## GET REST API to view all view list under 8Hrs
***************************
![automated testing](movielistunderhrs.png)
http://127.0.0.1:8000/api/movie-range-view/
● Will show the list of all movies which have diff of 8 hours between the ticket timing and current time.


## POST REST API to Delete all view list under 8Hrs
***************************
![automated testing](movielistdeleteunder8Hrs.png)
http://127.0.0.1:8000/api/movie-range-delete/
● Will DELETE the list of all movies which have diff of 8 hours between the ticket timing and current time.

## GET REST API to  get list of movie at the particular time
***************************
![automated testing](movielistwithparticulartime.png)
http://127.0.0.1:8000/api/avail-ticketlist/
● 

## GET REST API to get the list of all buyed tickets
***************************
![automated testing](ticketorderdlist.png)
http://127.0.0.1:8000/api/avail-ticketlist/
● 

## POST REST API to Update movie time
***************************
![automated testing](updatemoviedetails.png)
http://127.0.0.1:8000/api/avail-ticketlist/
● 

## GET REST API to get customer deatils by ticket ordered id
***************************
![automated testing](userdetailsbyticketid.png)
http://127.0.0.1:8000/api/avail-ticketlist/
● 
