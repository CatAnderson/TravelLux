from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)


# bucketlist homepage
@countries_blueprint.route("/bucket-list")
def destination():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("bucket_list/index.html", all_countries=countries, all_cities=cities)


# adding a destination - country page
@countries_blueprint.route("/bucket-list/add-destination")
def country_selection():
    countries = country_repository.select_all()
    return render_template("country/index.html", all_countries = countries)


@countries_blueprint.route("/bucket-list/add-destination/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('city/index.html', country=country)


# CREATE???


# edit your destination plans.
@countries_blueprint.route("/destination/<id>/edit", methods=['GET'])
def edit_destination(id):
    counrty = country_repository.select(id)
    cities = city_repository.select_all()
    return render_template('bucket_list/edit.html', country=country, cities=cities)


# updates the bucket list page with new city info?
@countries_blueprint.route("/destination/<id>", methods=['POST'])
def update_destination(id):
    name = request.form['city_name']
    visited = request.form['visited']
    counrty = city_repository.select(country_id)
    city = City(name, counrty, visited, id)
    city_repository.update(city)
    return redirect('/bucket_list')


# delete destination from bucketlist
@countries_blueprint.route("/bucket_list/<id>/delete", methods=['POST'])
def delete_destination(id):
    country_repository.delete(id)
    return redirect('/bucket-list')
