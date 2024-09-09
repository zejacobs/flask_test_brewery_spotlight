from flask import Flask
from getBreweryData import get_brewery_data

app = Flask(__name__)

@app.route("/")
def home():
    brewery_data = get_brewery_data()

    return brewery_data

if __name__ == '__main__':
    app.run(debug=True)