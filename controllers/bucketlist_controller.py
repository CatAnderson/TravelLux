from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.destination import Destination
from models.country import Country
from models.bucketlist import Bucketlist

import repositories.destination_repository as destination_repository
import repositories.country_repository as country_repository
import repositories.bucketlist_repository as bucketlist_repository

bucketlist_blueprint = Blueprint("bucketlist", __name__)


# bucketlist homepage
@bucketlist_blueprint.route("/bucketlist")
def destinations():
    bucketlists = bucketlist_repository.select_all()
    countries = country_repository.select_all()
    destinations = destination_repository.select_all()
    return render_template("bucketlist/index.html", countries=countries, destinations=destinations, bucketlists=bucketlists)
    

@bucketlist_blueprint.route("/bucketlist/<id>/delete", methods=['POST'])
def delete_bucketlist(id):
    bucketlist_repository.delete(id)
    return redirect('/bucketlist')


# @bucketlist_blueprint.route("/destination/<id>/edit")
# def edit_destination(id):
#     destination = destination_repository.select(id)
#     country = country_repository.select_all()
#     destinations = destination_repository.select_all()
#     return render_template('bucketlist/edit.html', country=country, destinations=destinations, bucketlist=bucketlist)


# @bucketlist_blueprint.route("/bucketlist/<id>", methods=['POST'])
# def update_bucketlist(id):
#     destination_id = request.form['destination']
#     destination_object = destination_repository.select(destination_id)
#     destination_name = destination_object.name
#     country_id = request.form['country']
#     country = country_repository.select(country_id)
#     visited = request.form['visited']

#     destination1 = Destination(destination_name, country, visited, id)
#     destination_repository.save(destination1)
#     new_destination = Bucketlist(destination1)

#     bucketlist_repository.update(new_destination)
#     return redirect('/bucketlist')

