from flask import Flask, render_template, request, redirect
from flask import Blueprint 

from models.review import Review
import repositories.review_repository as review_repository
import repositories.attraction_repository as attraction_repository

reviews_blueprint = Blueprint("reviews", __name__)

@reviews_blueprint.route("/reviews")
def reviews():
    reviews = review_repository.select_all()
    return render_template("reviews/index.html", reviews = reviews)

@reviews_blueprint.route("/reviews/<id>", methods=['GET'])
def show(id):
    review = review_repository.select(id)
    return render_template("reviews/show.html", review= review)

@reviews_blueprint.route("/reviews/<id>/edit", methods=['GET'])
def edit_review(id):
    review = review_repository.select(id)
    attractions = attraction_repository.select_all()
    return render_template("reviews/edit.html", review = review, attractions = attractions)

@reviews_blueprint.route("/reviews/<id>", methods=['POST'])
def update_review(id):
    title = request.form['title']
    content = request.form['content']
    attraction_id = request.form['attraction_id']
    attraction = attraction_repository.select(attraction_id)
    review = Review(title, content, attraction, id)
    review_repository.update(review)
    return redirect("/reviews")