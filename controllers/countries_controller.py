from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.country import Country
from models.destination import Destination

import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository

countries_blueprint = Blueprint("countries", __name__)





