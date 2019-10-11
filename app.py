from flask import Flask, Response, jsonify
from rank import load_json
import json

app = Flask(__name__)

@app.route('/films')
def films():
  films = load_json('json/films4.json')
  films.calculate_rank()
  resp = jsonify([films.__dict__])
  resp.status_code = 200
  return resp

@app.route('/films/comparisons')
def comparisons():
  films = load_json('json/films4.json')

  resp = jsonify([films.rank_data])
  resp.status_code = 200
  return resp

@app.route('/')
def hello():
    return 'Hello, World! This is Robin.'

@app.route('/robin')
def robin():
  return 'robin'