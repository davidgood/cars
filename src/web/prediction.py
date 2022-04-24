import locale
from flask import (
    Blueprint, url_for, request, redirect
)
from src.models import Predictor

bp = Blueprint('prediction', __name__, url_prefix='/prediction')


@bp.route('/price', methods=['POST'])
def price():
    vin = request.form['VIN']
    year = request.form['year']
    mileage = request.form['mileage']
    make = request.form.get('make')
    model = request.form.get('model')
    body = request.form.get('bodytype')
    horsepower = request.form['horsepower']
    city = request.form['cityfuel']
    highway = request.form['highwayfuel']
    engine = request.form.get('engine')
    fuel = request.form.get('fuel')
    transmission = request.form.get('transmission')
    seating = request.form['seating']

    p = Predictor(year, mileage, make, model, body, horsepower, city, highway, engine, fuel, transmission, seating)

    pr = p.predict_price()

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return f'Your price is: {locale.currency(float(pr), grouping=True)}'

