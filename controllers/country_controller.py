from flask import Flask, render_template, request, redirect
from flask import Blueprint 

from models.country import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show(id):
    country = country_repository.select(id)
    cities = country_repository.cities(country)
    return render_template("countries/show.html", country = country, cities = cities)

@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template("countries/edit.html", country = country)

@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['name']
    visited = request.form['visited']
    wishlist = request.form['wishlist']
    country = Country(name, visited, wishlist, id)
    country_repository.update(country)
    return redirect('/countries')