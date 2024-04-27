from flask import (
    Blueprint, render_template, jsonify
)

from app.services import is_double_yesterday

bp = Blueprint('double', __name__)

@bp.route('/')
def index():
    return render_template('double/index.html')

@bp.route('/_internal/get_double_data')
def get_double_data():
    result = is_double_yesterday()
    return result