from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
from models.destination import Destination

import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("country/index.html", all_countries = countries)

# NEW
# GET
@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    countries = ountry_repository.select_all()
    return render_template("country/new.html", all_countries = countries)


# CREATE
# POST '/tasks'
@countries_blueprint.route("/countries",  methods=['POST'])
def create_country():
    name = request.form['country_name']
    continent = request.form['continent']
    country = Country(name, continent)
    country_repository.save(country)
    return redirect('/countries')
