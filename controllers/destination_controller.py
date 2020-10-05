from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.destination import Destination
from models.country import Country

import repositories.destination_repository as destination_repository
import repositories.country_repository as country_repository

destinations_blueprint = Blueprint("destinations", __name__)


# bucketlist homepage
@destinations_blueprint.route("/bucket-list")
def destination():
    countries = country_repository.select_all()
    destinations = destination_repository.select_all()
    return render_template("bucket_list/index.html", all_countries=countries, all_destinations=destination)


# adding a destination - country page
@destinations_blueprint.route("/destination/new/countries")
def country_selection():
    countries = country_repository.select_all()
    return render_template("country/index.html", all_countries = countries)


@destinations_blueprint.route("/destination/new/<id>", methods=['GET'])
def create_destination(id):
    country = country_repository.select(id)
    name = request.form['destination']
    country = destination_repository.select(destination.country.id)
    visited = request.form['visited']
    destination = Destination(name, country, visited)
    destination_repository.save(destination)
    return render_template('destination/index.html', country=country, all_destinations=destination)


# edit your destination plans.
@destinations_blueprint.route("/destination/<id>/edit", methods=['GET'])
def edit_destination(id):
    counrty = country_repository.select(id)
    destinations = destination_repository.select_all()
    return render_template('bucket_list/edit.html', country=country, destinations=destinations)


# updates the bucket list page with new city info?
@destinations_blueprint.route("/destination/<id>", methods=['POST'])
def update_destination(id):
    name = request.form['destination']
    visited = request.form['visited']
    counrty = city_repository.select(country_id)
    destination = Destination(name, counrty, visited, id)
    destination_repository.update(destination)
    return redirect('/bucket_list')


# delete destination from bucketlist
@destinations_blueprint.route("/destination/<id>/delete", methods=['POST'])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect('/bucket-list') 