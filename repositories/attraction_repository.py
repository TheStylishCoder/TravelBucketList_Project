from db.run_sql import run_sql
from models.attraction import Attraction
from models.city import City 
import repositories.city_repository as city_repository

def save(attraction):
    sql = "INSERT INTO attractions (name, category, city_id, entry_fee) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [attraction.name, attraction.category, attraction.city.id, attraction.entry_fee]
    results = run_sql(sql, values)
    id = results[0]['id']
    attraction.id = id
    return attraction

def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql) 

def delete(id):
    sql = "DELETE FROM attractions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    attractions = []
    sql = "SELECT * FROM attractions ORDER BY category"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], row['category'], city, row['entry_fee'], row['id'])
        attractions.append(attraction)
    return attractions

def select(id):
    attraction = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(result['city_id'])
        attraction = Attraction(result['name'], result['category'], city, result['entry_fee'], result['id'])
    return attraction

def update(attraction):
    sql = "UPDATE attractions SET (name, category, city_id, entry_fee) = (%s, %s, %s, %s) WHERE id = %s "
    values = [attraction.name, attraction.category, attraction.city.id, attraction.entry_fee, attraction.id]
    run_sql(sql, values)

def free_entry():
    attractions = []

    sql = "SELECT * FROM attractions WHERE entry_fee = %s ORDER BY category"
    values = [False]
    results = run_sql(sql, values)

    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], row['category'], city, row['entry_fee'], row['id'])
        attractions.append(attraction)
    return attractions

def search(search):
    attractions = []
    sql = "SELECT * FROM attractions WHERE category iLIKE %s"
    values = [f'%{search}%']
    results = run_sql(sql, values)

    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], row['category'], city, row['entry_fee'], row['id'])
        attractions.append(attraction)
    return attractions