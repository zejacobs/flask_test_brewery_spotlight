from flask import Blueprint, render_template
from getBreweryData import get_brewery_data

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    brewery_data = get_brewery_data()

    return render_template("index.html", brewery_data=brewery_data)