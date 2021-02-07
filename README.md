# TravelBucketList_Project

Codeclan Solo Project 


## Travel Bucket List Brief:-

Build an app to track someone's travel adventures.

### MVP:

 * The app should allow the user to track countries and cities they want to visit and those they have visited.
 * The user should be able to create and edit countries
 * Each country should have one or more cities to visit
 * The user should be able to create and delete entries for cities
 * The app should allow the user to mark destinations as visited or still to see

### Possible Extensions:

 * Have separate pages for destinations visited and those still to visit
 * Add sights to the destination cities
 * Search for destination by continent, city or country
 * Any other ideas you might come up with
 
 
 ## Running Instructions
* After cloning the repository, create a database called "travel list" in PostgreSQL. This can be done with the command createdb travel_list. 
* Then run the SQL file included to create the tables required. From the directory that this readme file is in, this can be achieved by runnning the command psql -d travel_list -f app/db/travel_list.sql. Seed data has been saved in the 'console.py' file.
* To start the app, use the command 'flask run' once the first steps are completed. The app can be accessed in your browser at the port specified by your flask instance.
 
 
 ## Requirements:
 * Python3
 * pip3
 * psycopg2
 * Flask
 * PostgreSQL
 
 ## How To Clone:
 Clone repo: $ https://github.com/TheStylishCoder/TravelBucketList_Project.git.

 
 
 
