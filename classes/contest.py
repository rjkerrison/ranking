import json

class Contest():
  def __init__(self, *args, **kwargs):
    if len(args) >= 2:
      self.contestors = frozenset(args[:2])

    if len(args) >= 3:
      self.outcome = args[2]

    if 'contestors' in kwargs:
      self.contestors = frozenset(kwargs['contestors'])

    if 'outcome' in kwargs:
      self.outcome = kwargs['outcome']

  def __eq__(self, a):
    return (
      isinstance(a, Contest)
      and a.contestors == self.contestors
      and a.outcome == self.outcome
    )

  def as_json(self):
    return json.dumps({
      'contestors': list(self.contestors),
      'outcome': self.outcome
    })
