/*
a) 	The information included in the columns table nested inside actors table is
	actor__id, first_name, last_name, and last_update.
b)	The information included in the columns table nested inside film table is
	film_id, title, description, release_year, language_id, original_language_id,
    rental_duration, rental_rate, length, replacement_cost, rating, special_features,
    and last_update.
c)	The only other table that contains columns for both actor_id and film_id is film_actor.
d)	The rental table includes information on who rented a film, what film they rented,
	an id number for the rental (like a receipt), what day and time, the worker
	that attended them and when the last update was made. This information is easy to read
    as it is structured in an organized way although admittedly the information was bit
    overwhelming at first due to the large amount of records.
e)	This table includes inventory id, film id, store id, and last update.
f)	In order to understand the names of all films that were rented on a specific date,
	we need to use the film table and the rental table. They are related to each other
    because the rental table references the film table such as film id (which in the film
    table helps us identify the film) and the film table contains key information for 
    rentals such as rental duration and rental rate.
*/
SELECT title FROM film;
SELECT film_id FROM  film;
SELECT rental_date FROM rental;
SELECT inventory_id FROM rental;
