from flask import Flask, render_template, request, redirect
from flask import Blueprint 

from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show(id):
    city = city_repository.select(id)
    attractions = city_repository.attractions(city)
    return render_template("cities/show.html", city = city, attractions = attractions)

@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("cities/edit.html", city = city, countries = countries)

@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    wishlist = request.form['wishlist']
    country = country_repository.select(country_id)
    city = City(name, country, visited, wishlist, id)
    city_repository.update(city)
    return redirect("/cities")