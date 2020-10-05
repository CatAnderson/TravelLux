from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)


@countries_blueprint.route("/countries")
def tasks():
    countries = country_repository.select_all()
    return render_template("country/index.html", all_countries = countries)


@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('city/index.html', country = country)
