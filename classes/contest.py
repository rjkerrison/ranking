import json
import hashlib

class Contest():
  def __init__(self, *args, **kwargs):
    self.contestants = []
    self.outcome = ''

    if len(args) >= 2:
      self.contestants = frozenset(args[:2])

    if len(args) >= 3:
      self.outcome = args[2]

    if 'contestants' in kwargs:
      self.contestants = frozenset(kwargs['contestants'])

    if 'outcome' in kwargs:
      self.outcome = kwargs['outcome']

    self._id = self._generate_unique_id()

  def __eq__(self, a):
    return (
      isinstance(a, Contest)
      and a.contestants == self.contestants
      and a.outcome == self.outcome
    )

  def _generate_unique_id(self):
    json_to_encode = json.dumps(list(self.contestants))
    encoded_json = json_to_encode.encode('ascii')
    return hashlib.sha1(encoded_json).hexdigest()

  def as_dict(self):
    return {
      '_id': self._id,
      'contestants': list(self.contestants),
      'outcome': self.outcome
    }

  def as_json(self):
    return json.dumps(self.as_dict())

  @staticmethod
  def from_json(json_contest):
    return Contest(**json.loads(json_contest))
