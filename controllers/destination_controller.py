from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.destination import Destination
from models.country import Country
from models.bucketlist import Bucketlist

import repositories.destination_repository as destination_repository
import repositories.country_repository as country_repository
import repositories.bucketlist_repository as bucketlist_repository

destinations_blueprint = Blueprint("destinations", __name__)
# bucketlist_blueprint = Blueprint("bucektlist", __name__)


# adding a destination - country page
@destinations_blueprint.route("/destination/new/countries")
def country_selection():
    countries = country_repository.select_all()
    return render_template("country/index.html", all_countries = countries)


@destinations_blueprint.route("/destination/new/<country_id>")
def create_destination_from_id(country_id):
    country = country_repository.select(country_id)
    destination = destination_repository.select_all()
    # destination_name = request.form['destination']
    # country = destination_repository.select(destination.country.id)
    # visited = request.form['visited']
    # destination = Destination(destination_name, country, visited)
    # destination_repository.save(destination)
    return render_template('destination/index.html', country=country, destinations=destination)

@destinations_blueprint.route("/bucketlist", methods=["POST"])
def create_destination():
    destination_id = request.form['destination']
    destination_object = destination_repository.select(destination_id)
    destination_name = destination_object.name
    country_id = request.form['country']
    country = country_repository.select(country_id)
    visited = request.form['visited']

    destination1 = Destination(destination_name, country, visited)
    destination_repository.save(destination1)
    new_destination = Bucketlist(destination1)

    bucketlist_repository.save(new_destination)

    return redirect("/bucketlist")

# edit your destination plans.
@destinations_blueprint.route("/destination/<id>/edit", methods=['GET'])
def edit_destination(id):
    country = country_repository.select(id)
    destinations = destination_repository.select_all()
    return render_template('bucketlist/edit.html', country=country, destinations=destinations)


# updates the bucket list page with new city info?
@destinations_blueprint.route("/destination/<id>", methods=['POST'])
def update_destination(id):
    destination_name = request.form['destination']
    visited = request.form['visited']
    country = destination_repository.select(country_id)
    destination = Destination(destination_name, country, visited, id)
    destination_repository.update(destination)
    return redirect('/bucketlist')


# delete destination from bucketlist
@destinations_blueprint.route("/destination/<destination_id>/delete", methods=['POST'])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect('/bucket-list') 