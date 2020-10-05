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
@countries_blueprint.route("/countries",  methods=['POST'])
def create_country():
    name = request.form['country_name']
    continent = request.form['continent']
    country = Country(name, continent)
    country_repository.save(country)
    return redirect('/countries')



# SHOW
@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('country/show.html', country=country)
 

# EDIT
@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    destinations = destination_repository.select()
    return render_template('counrty/edit.html', destinations = destination, country = country)


# UPDATE
@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['country_name']
    continent = request.form['continent']
    country = Country(name, continent)
    country_repository.update(country)
    return redirect('/countries')


# DELETE
@tasks_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_counrty(id):
    country_repository.delete(id)
    return redirect('/counrties')
