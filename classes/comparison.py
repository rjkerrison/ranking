import datetime
import enum

class Ordering(enum.Enum):
    OneBeatsTwo = -1
    OnAPar = 0
    TwoBeatsOne = 1

class Comparison():
    def __init__(self, pair, choice):
        self.pair = pair
        self.choice = choice
        self.time = datetime.datetime.now()

class ComparisonBuilder():
    def __init__(self):
        return

    def build_comparison(self, pair, choice):
        try:
            pair = [a for a in pair]
        except Exception as e:
            raise Exception(f'{pair} is not an iterable.', e)

        if len(pair) != 2:
            raise Exception(f'{pair} is not an iterable of length 2.')

        try:
            choice = Ordering(choice)
        except:
            try:
                choice = int(choice)
                choice = Ordering(choice)
            except:
                raise Exception(f'{choice} is an invalid ordering.')

        return Comparison(pair, choice)
