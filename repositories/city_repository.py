from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.attraction import Attraction

import repositories.country_repository as country_repository



def save(city):
    sql = "INSERT INTO cities (name, country_id, visited, wishlist) VALUES (%s, %s, %s, %s) RETURNING * "
    values = [city.name, city.country.id, city.visited, city.wishlist]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql) 

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    cities = []
    sql = "SELECT * FROM cities ORDER BY name"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['wishlist'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['name'], country, result['visited'], result['wishlist'], result['id'])
    return city 

def update(city):
    sql = "UPDATE cities SET (name, country_id, visited, wishlist) = (%s, %s, %s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.visited, city.wishlist, city.id]
    run_sql(sql, values)

def attractions(city):
    attractions = []

    sql = "SELECT * FROM attractions WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        attraction = Attraction(row['name'], row['category'], row['city_id'], row['entry_fee'], row['id'])
        attractions.append(attraction)
    return attractions

def visited():
    cities = []

    sql = "SELECT * FROM cities WHERE visited = %s ORDER BY name"
    values = [True]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['wishlist'], row['id'])
        cities.append(city)
    return cities 

def wishlist():
    cities = []

    sql = "SELECT * FROM cities WHERE wishlist = %s ORDER BY name"
    values = [True]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['wishlist'], row['id'])
        cities.append(city)
    return cities

def search(search):
    cities = []
    sql = "SELECT * FROM cities WHERE name iLIKE %s"
    values = [f'%{search}%']
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['wishlist'], row['id'])
        cities.append(city)
    return cities