import json

class Contest():
  def __init__(self, *args, **kwargs):
    if len(args) >= 2:
      self.contestants = frozenset(args[:2])

    if len(args) >= 3:
      self.outcome = args[2]

    if 'contestants' in kwargs:
      self.contestants = frozenset(kwargs['contestants'])

    if 'outcome' in kwargs:
      self.outcome = kwargs['outcome']

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
