# Movie-theatre-ticket-booking-system_Backend
 
 **TECH STACK**
 Python, Django(Framework), SQLite database
 
 ## SQLite database
 ***************************
 ![automated testing](sql.png)
 <ul>
  <li>Customer table     (ID,Name,phone number,time)</li>
  <li>Movie table        (ID,Movie name,Movie time)</li>
  <li>Ticket Order table (ID,Customer key,Movie key,Quantity of tickets ordered<=20)</li>
</ul>

 
 
 ## Rest API Overview
 ***************************
 ![automated testing](apioverview.png)
 http://127.0.0.1:8000/api/
  <ul>
  <li>Contain the list of all rest api created</li>
</ul>

 
 
 
 ## Show all Avail Movies list
 ***************************
![automated testing](availmovieslist.png)
http://127.0.0.1:8000/api/avail-ticketlist/
  <ul>
  <li>Api will show the list of all the movie available to buy.</li>
</ul>

## POST REST API to Buy tickets
***************************
![automated testing](buyticket.png)
http://127.0.0.1:8000/api/buy-ticket/
  <ul>
  <li>Post api to buy tickets not more than 20 tickets.</li>
 <li>{ "tickets_quantity": 5,"customer": 1,"movie_detail": 1}</li>
 <li>Ask for customer id,movie id and number of tickets wants to buy.</li>
 <li>Ticket order id will be automatically updated.</li>
 <li>Ticket quantity can't be more than 20 (validation)</li>
</ul>

## POST REST API Delete Ticket
***************************
![automated testing](moviedeletebymovieid.png)
http://127.0.0.1:8000/api/movie-delete/<str:Mid>/
<ul>
 <li>Post api ask for movie id to detele is from database.</li>
</ul>



## GET REST API to get buyed Movie details by ordered ticket ID
***************************
![automated testing](moviedetailbymovieid.png)
http://127.0.0.1:8000/api/movie-details/<str:Mid>/
<ul>
 <li>Post api to get details of movie from ordered ticket's ID</li>
</ul>


## GET REST API to view all view list under 8Hrs
***************************
![automated testing](movielistunderhrs.png)
http://127.0.0.1:8000/api/movie-range-view/
<ul>
 <li> Will show the list of all movies which have diff of 8 hours between the ticket timing and current time.</li>
</ul>



## POST REST API to Delete all view list under 8Hrs
***************************
![automated testing](movielistdeleteunder8Hrs.png)
http://127.0.0.1:8000/api/movie-range-delete/
<ul>
 <li>Will DELETE the list of all movies which have diff of 8 hours between the ticket timing and current time.</li>
</ul>


## GET REST API to  get list of movie at the particular time
***************************
![automated testing](movielistwithparticulartime.png)
http://127.0.0.1:8000/api/avail-ticketlist/
<ul>
 <li>Will return json reponse list of all the movie having same data time</li>
</ul>

## GET REST API to get the list of all buyed tickets
***************************
![automated testing](ticketorderdlist.png)
http://127.0.0.1:8000/api/avail-ticketlist/
<ul>
 <li>will return details of all the buyed tickes</li>
</ul>

## POST REST API to Update movie time
***************************
![automated testing](updatemoviedetails.png)
http://127.0.0.1:8000/api/avail-ticketlist/
<ul>
 <li>POST Rest Api to update movie name and time</li>
 <li>{"movie_name": "Kedarnath","movie_time": "2020-08-31T12:00:00Z"}</li>
 <li>Movie id will automatically update</li>
</ul>

## GET REST API to get customer deatils by ticket ordered id
***************************
![automated testing](userdetailsbyticketid.png)
http://127.0.0.1:8000/api/avail-ticketlist/
<ul>
 <li>to get the customer details from orderd ticket id</li>
</ul>
