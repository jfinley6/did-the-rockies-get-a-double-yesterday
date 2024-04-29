import os

from flask import Flask, render_template
from services import is_double_yesterday


# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/')
def index():
    return render_template('double/index.html')

@app.route('/_internal/get_double_data')
def get_double_data():
    result = is_double_yesterday()
    return result
