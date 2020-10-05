from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/bucket-list/add-destination/city")
def city_selection():
    cities = city_repository.select_all()
    return render_template("city/index.html", all_cities = cities)

@cities_blueprint.route("/bucket-list/new-destination",  methods=['POST'])
def create_destination():
    city_name = request.form['city']
    country = city_repository.select(city.country.id)
    visited = request.form['visited']
    city = City(description, country, visited)
    city_repository.save(city)
    return redirect('/bucketlist')