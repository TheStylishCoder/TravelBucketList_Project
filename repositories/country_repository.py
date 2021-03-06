from db.run_sql import run_sql
from models.country import Country 
from models.city import City

def save(country):
    sql = "INSERT INTO countries (name, visited, wishlist) VALUES (%s, %s, %s) RETURNING * "
    values = [country.name, country.visited, country.wishlist]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id 
    return country 

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    countries = []
    sql = "SELECT * FROM countries ORDER BY name"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['visited'], row['wishlist'], row['id'])
        countries.append(country)
    return countries 

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['visited'], result['wishlist'], result['id'])
    return country 

def update(country):
    sql = "UPDATE countries SET (name, visited, wishlist) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.visited, country.wishlist, country.id]
    run_sql(sql, values)

def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['country_id'], row['visited'], row['wishlist'], row['id'])
        cities.append(city)
    return cities 

def visited():
    countries = []

    sql = "SELECT * FROM countries WHERE visited = %s ORDER BY name"
    values = [True]
    results = run_sql(sql, values)

    for row in results:
        country = Country(row['name'], row['visited'], row['wishlist'], row['id'])
        countries.append(country)
    return countries

def wishlist():
    countries = []

    sql = "SELECT * FROM countries WHERE wishlist = %s ORDER BY name"
    values = [True]
    results = run_sql(sql, values)

    for row in results:
        country = Country(row['name'], row['visited'], row['wishlist'], row['id'])
        countries.append(country)
    return countries

def search(search):
    countries = []
    sql = "SELECT * FROM countries WHERE name iLIKE %s"
    values = [f'%{search}%']
    results = run_sql(sql, values)

    for row in results:
        country = Country(row['name'], row['visited'], row['wishlist'], row['id'])
        countries.append(country)
    return countries