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

def delete_all():
    sql = "DELETE FROM reviews"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM reviews where id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    reviews = []
    sql = "SELECT * FROM reviews"
    results = run_sql(sql)

    for row in results:
        attraction = attraction_repository.select(row['attraction_id'])
        review = Review(row['title'], row['content'], attraction, row['id'])
        reviews.append(review)
    return reviews

def select(id):
    review = None
    sql = "SELECT * FROM reviews WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        attraction = attraction_repository.select(result['attraction_id'])
        review = Review(result['title'], result['content'], attraction, result['id'])
    return review 

def update(review):
    sql = "UPDATE reviews SET (title, content, attraction_id) = (%s, %s, %s) WHERE id = %s"
    values = [review.title, review.content, review.attraction.id, review.id]
    run_sql(sql, values)