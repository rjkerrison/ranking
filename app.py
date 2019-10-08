from flask import Flask, Response
from rank import load_json
import json

app = Flask(__name__)

@app.route('/films')
def films():
  films = load_json('json/films4.json')
  films.calculate_rank()
  json_response = json.dumps([films.__dict__])

  resp = Response(json_response, status=200, mimetype='application/json')

  return resp

@app.route('/')
def hello():
    return 'Hello, World! This is Robin.'

@app.route('/robin')
def robin():
  return 'robin'