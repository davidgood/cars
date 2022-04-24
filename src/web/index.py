import jsonify as jsonify
from flask import (
    Blueprint, render_template, request, redirect
)

from src.models import Predictor
from src.web.db import get_db

bp = Blueprint('index', __name__, url_prefix='/')


def get_list(query):
    db = get_db()
    lst = db.execute(query).fetchall()
    return lst


def get_list_with_parms(query, parms):
    db = get_db()
    lst = db.execute(query, parms).fetchall()
    return lst


@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        vin = request.form['VIN']
        db = get_db()
        error = None

    makes = get_list("SELECT id, name FROM makes ORDER BY name;")
    models = get_list("SELECT id, name FROM models ORDER BY name;")
    bodies = get_list("SELECT id, name FROM bodytypes ORDER BY name;")
    engines = get_list("SELECT id, name FROM enginetypes ORDER BY name;")
    fuels = get_list("SELECT id, name FROM fueltypes ORDER BY name;")
    transmissions = get_list("SELECT id, name FROM transmissions ORDER BY name;")

    return render_template('index.html',
                           makes_list=makes,
                           models_list=models,
                           body_list=bodies,
                           engine_list=engines,
                           fuel_list=fuels,
                           trans_list=transmissions)


@bp.route('/get_models/<make>')
def get_food(make):
    try:
        db = get_db()
        models = db.execute("SELECT id, name FROM models WHERE makeid = ? ORDER BY name;", (make,)).fetchall()

        ret = ''
        for entry in models:
            ret += f'<option value="{entry[0]}">{entry[1]}</option>'
        return ret
    except Exception as err:
        print(err)



