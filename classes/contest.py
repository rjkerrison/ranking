import json

class Contest():
  def __init__(self, *args, **kwargs):
    if 'contestants' in kwargs:
      contestants = kwargs['contestants']
    else:
      contestants = [c for c in args if isinstance(c, Contestant)]

    if 'outcome' in kwargs:
      outcomes = [kwargs['outcome']]
    else:
      outcomes = [o for o in args if isinstance(o, Outcome)]

    if len(contestants) == 2:
      self.contestants = frozenset(contestants)

    if len(outcomes) == 1:
      self.outcome = outcomes[0]

  def __eq__(self, a):
    return (
      isinstance(a, Contest)
      and a.contestants == self.contestants
      and a.outcome == self.outcome
    )

  def as_json(self):
    return json.dumps({
      'contestants': list(self.contestants),
      'outcome': self.outcome
    })

  @staticmethod
  def from_json(json_contest):
    return Contest(**json.loads(json_contest))

class Contestant():
  def __init__(self, id, **kwargs):
    self.id = id
    self.details = kwargs

class Outcome():
  pass

class Win(Outcome):
  def __init__(self, winner):
    if not isinstance(winner, Contestant):
      raise Exception(f'{winner} is not a Contestant')

class Draw(Outcome):
  pass

class Unknown(Outcome):
  pass