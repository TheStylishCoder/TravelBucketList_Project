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