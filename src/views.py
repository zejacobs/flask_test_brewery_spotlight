from flask import Blueprint, render_template
from getBreweryData import *

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    brewery_data = get_random_brewery()

    return render_template("index.html", brewery_data=brewery_data)