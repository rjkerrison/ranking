from flask import Flask, Response, jsonify
from rank import load_json
import json

app = Flask(__name__)
films = load_json('json/films5.json')

@app.route('/films')
def films_index():
  films.calculate_rank()
  resp = jsonify([films.__dict__])
  resp.status_code = 200
  return resp

@app.route('/films/comparisons/', defaults ={'id': None})
@app.route('/films/comparisons/<string:id>')
def comparisons(id):
  c = films.get_comparisons()

  if id is not None:
    resp = jsonify(c[id].serialize())
  else:
    resp = jsonify({f:c[f].serialize() for f in c})

  resp.status_code = 200
  return resp

@app.route('/films/comparisons/<string:id1>/beats/<string:id2>', methods = ['POST'])
def beats(id1, id2):
  comparison = f'{id1}>{id2}'
  films.rank_data.append(comparison)

  resp = Response()
  resp.status_code = 200
  return resp

@app.route('/films/scores/', defaults ={'id': None})
@app.route('/films/scores/<string:id>')
def scores(id):
  c = films.get_comparisons()

  if id is not None:
    resp = jsonify(c[id].score())
  else:
    resp = jsonify({f:c[f].score() for f in c})

  resp.status_code = 200
  return resp

@app.route('/')
def hello():
    return 'Hello, World! This is Robin.'

@app.route('/robin')
def robin():
  return 'robin'