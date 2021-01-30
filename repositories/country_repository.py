from db.run_sql import run_sql
from models.country import Country 

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