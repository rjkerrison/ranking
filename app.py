from flask import Flask, Response, jsonify
from rank import load_json
import json

app = Flask(__name__)

@app.route('/films')
def films():
  films = load_json('json/films5.json')
  films.calculate_rank()
  resp = jsonify([films.__dict__])
  resp.status_code = 200
  return resp

@app.route('/films/comparisons/', defaults ={'id': None})
@app.route('/films/comparisons/<string:id>')
def comparisons(id):
  films = load_json('json/films5.json')
  c = films.get_comparisons()

  if id is not None:
    resp = jsonify(c[id].serialize())
  else:
    resp = jsonify({f:c[f].serialize() for f in c})

  resp.status_code = 200
  return resp

@app.route('/')
def hello():
    return 'Hello, World! This is Robin.'

@app.route('/robin')
def robin():
  return 'robin'