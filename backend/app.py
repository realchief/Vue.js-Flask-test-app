import os
from flask import Flask, request, redirect, jsonify
from flask_cors import CORS

import requests

from models import Variation, db

from dotenv import load_dotenv

load_dotenv(verbose=True, dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config.update(
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SECRET_KEY=os.getenv('SECRET_KEY')
)

db.init_app(app)


search_url_template = u'https://www.google.com/search?q={}&oq={}'

@app.route('/api/variations', methods=('GET',))
def get_variations():
    # TODO: query the database using the Flask-SQLAlchemy model defined in models.py
    # and return them in a serialized list using the to_dict() method of the Variation model
    variation = Variation()
    dict= variation.to_dict()
    return jsonify(dict)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
