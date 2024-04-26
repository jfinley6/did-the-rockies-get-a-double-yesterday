from flask import (
    Blueprint, render_template
)

from app.services import is_double_yesterday

bp = Blueprint('double', __name__)

@bp.route('/')
def index():
    return render_template('double/index.html', double=is_double_yesterday())