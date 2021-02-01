from flask import Flask, render_template, request, redirect
from flask import Blueprint 

from models.attraction import Attraction
import repositories.attraction_repository as attraction_repository
import repositories.city_repository as city_repository

attractions_blueprint = Blueprint("attractions", __name__)

@attractions_blueprint.route("/attractions")
def attractions():
    attractions = attraction_repository.select_all()
    return render_template("attractions/index.html", attractions = attractions)

@attractions_blueprint.route("/attractions/<id>", methods=['GET'])
def show(id):
    attraction = attraction_repository.select(id)
    return render_template("attractions/show.html", attraction = attraction)

@attractions_blueprint.route("/attractions/<id>/edit", methods=['GET'])
def edit_attraction(id):
    attraction= attraction_repository.select(id)
    cities = city_repository.select_all()
    return render_template("attractions/edit.html", attraction = attraction, cities = cities)

@attractions_blueprint.route("/attractions/<id>", methods=['POST'])
def update_attraction(id):
    name = request.form['name']
    category = request.form['category']
    city_id = request.form['city_id']
    entry_fee = request.form['entry_fee']
    city = city_repository.select(city_id)
    attraction = Attraction(name, category, city, entry_fee, id)
    attraction_repository.update(attraction)
    return redirect("/attractions")

@attractions_blueprint.route("/attractions/new", methods=['GET'])
def new_attraction():
    cities = city_repository.select_all()
    return render_template("attractions/new.html", cities = cities)

@attractions_blueprint.route("/attractions", methods=['POST'])
def create_attraction():
    name = request.form['name']
    category= request.form['category']
    city_id = request.form['city_id']
    entry_fee = request.form['entry_fee']
    city = city_repository.select(city_id)
    attraction = Attraction(name, category, city, entry_fee)
    attraction_repository.save(attraction)
    return redirect('/attractions')

@attractions_blueprint.route("/attraction/<id>/delete", methods=['POST'])
def delete_attraction(id):
    attraction_repository.delete(id)
    return redirect('/attractions')

@attractions_blueprint.route("/attractions/free", methods=['GET'])
def show_free():
    attractions = attraction_repository.free_entry()
    return render_template("attractions/show_free.html", attractions = attractions)

@attractions_blueprint.route("/attractions/search", methods=['GET'])
def search_for_attraction():
    return render_template("attractions/search.html")

@attractions_blueprint.route("/attractions/search_results", methods=['POST'])
def search_results():
    search = request.form['search']
    attractions = attraction_repository.search(search)
    return render_template("/attractions/search_results.html", attractions = attractions)

