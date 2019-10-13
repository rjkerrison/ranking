import itertools
from .contest import Contest

songs = [
  'Elephant by Tame Impala',
  'Cosmic Dancer by T. Rex',
  'On My Way by Rusted Root',
  'Into You by Ariana Grande',
  'Dear Prudence by The Beatles',
  'Immigrant Song by Led Zeppelin',
  'Paint It Black by The Rolling Stongs',
  'From The Ritz To The Rubble by Arctic Monkeys'
]

contests = []

for contestant_pair in itertools.combinations(songs, 2):
  contest = Contest(contestants = contestant_pair)
  contests.append(contest)

def set_winner(id, winner):
  contests_with_id = [c for c in contests if c._id == id]
  if len(contests_with_id) == 1:
    contests_with_id[0].outcome = winner
