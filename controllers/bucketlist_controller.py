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