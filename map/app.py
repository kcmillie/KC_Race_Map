
import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL


import json

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'carmen_races_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


# this route will test the database connection and nothing more
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/all_races")
def all_races():
	"""returns brewery list"""
	conn = mysql.connect()
	cursor =conn.cursor()

	cursor.execute("SELECT * from races")
	data = cursor.fetchall()

	races = []
	for x in data:
		race = {}
		race["name"] = x[0]
		race["date"] = x[1]
		# race["finish time"] = x[2]/,.	
		races.append(race)

    # Return a list of the column names (sample names)
	return json.dumps(races)


if __name__ == '__main__':
    app.run(debug=True)