from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from src.web.db import get_db

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        vin = request.form['VIN']
        db = get_db()
        error = None

    return render_template('index.html')
