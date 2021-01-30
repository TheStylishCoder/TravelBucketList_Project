from db.run_sql import run_sql

from models.review import Review
from models.attraction import Attraction

import repositories.attraction_repository as attraction_repository

def save(review):
    sql = "INSERT INTO reviews (title, content, attraction_id) VALUES (%s, %s, %s) RETURNING *"
    values = [review.title, review.content, review.attraction.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    review.id = id
    return review 