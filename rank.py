import json
import random
import re
from classes import ranking

all_rankings = {}

def load_json(json_file):
    rankin = ranking.get_ranking_from_json(json_file)
    all_rankings[rankin.name] = rankin
    return rankin

def save_json(ranking_name, json_file):
    ranking.save_ranking_to_json(all_rankings[ranking_name], json_file)

def get_ranking(name):
    global all_rankings

    if name not in all_rankings:
        raise Error('Json not loaded')
    return all_rankings[name]

def choose_ranking(ranking):
    a, b = random.choice(ranking.entries), random.choice(ranking.entries)
    print('A: {name}, {director}'.format(**a))
    print('B: {name}, {director}'.format(**b))

    choice_made = None

    while choice_made is None:

        choice_made = input('Make a choice, "A", "B" or "=": ')

        if re.match('^[A=B]$', choice_made):
            ranking.add_comparison('{a_id}{choice_made}{b_id}'.format(
                a_id = a['_id'],
                choice_made = {'A': '>', '=': '=', 'B': '<'}[choice_made],
                b_id = b['_id']))

        else:
            choice_made = None

def main():
    films = load_json('json/films4.json')

    choose = True
    while choose:
        choose_ranking(films)
        choose = 'y' in input('Continue? (y/n) ')

    films.calculate_rank()

    save_json('films', 'json/films5.json')

if __name__ == '__main__':
    main()
