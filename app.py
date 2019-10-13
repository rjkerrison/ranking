from flask import Flask, Response, jsonify, request, render_template
from rank import load_json
from classes import songs
import json

app = Flask(
  __name__,
  static_folder='./static/dist',
  template_folder='./static')

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
  return render_template('./index.html')

@app.route('/songs')
def get_songs():
  return jsonify(songs.songs)

@app.route('/songs/contests')
def get_songs_contests():
  return jsonify([c.as_dict() for c in songs.contests])

@app.route('/songs/contests/<string:id>', methods = ['GET', 'POST'])
def post_winner(id):
  print({
    'form': request.form,
    'json': request.json
  })

  if request.method == 'POST':
    winner = request.json['winner']
    songs.set_winner(id, winner)

  resp = jsonify([a.as_dict() for a in songs.contests if a._id == id])
  return resp

@app.route('/songs/scores')
def get_songs_scores():
  scores = {}

  for song in songs.songs:
    song_wins = 0
    song_losses = 0

    song_contests = (c for c in songs.contests if song in c.contestants)
    for contest in song_contests:
      if song == contest.outcome:
        song_wins += 1
      elif contest.outcome:
        song_losses += 1

    scores[song] = song_wins - song_losses

  return jsonify(scores)
