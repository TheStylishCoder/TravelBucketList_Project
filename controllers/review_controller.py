from flask import Flask, render_template, request, redirect
from flask import Blueprint 

from models.review import Review
import repositories.review_repository as review_repository
import repositories.attraction_repository as attraction_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

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

@reviews_blueprint.route("/reviews/new", methods=['GET'])
def new_review():
    attractions = attraction_repository.select_all()
    return render_template("reviews/new.html", attractions = attractions)

@reviews_blueprint.route("/reviews", methods=['POST'])
def create_review():
    title = request.form['title']
    content= request.form['content']
    attraction_id = request.form['attraction_id']
    attraction = attraction_repository.select(attraction_id)
    review = Review(title, content, attraction)
    review_repository.save(review)
    return redirect('/reviews')

@reviews_blueprint.route("/review/<id>/delete", methods=['POST'])
def delete_review(id):
    review_repository.delete(id)
    return redirect('/reviews')

@reviews_blueprint.route("/review/visited", methods=['GET'])
def show_visited():
    countries = country_repository.visited()
    cities = city_repository.visited()
    return render_template("visited/index.html", countries = countries, cities = cities)

@reviews_blueprint.route("/review/wishlist", methods=['GET'])
def show_wishlist():
    countries = country_repository.wishlist()
    cities = city_repository.wishlist()
    return render_template("wishlist/index.html", countries = countries, cities = cities)