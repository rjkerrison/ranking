import json
import random
import re
from classes import ranking, file_handler

all_rankings = {}

def load_json(json_file):
    rankin = file_handler.get_ranking_from_json(json_file)
    all_rankings[rankin.name] = rankin
    return rankin

def save_json(ranking_name, json_file):
    file_handler.save_ranking_to_json(all_rankings[ranking_name], json_file)

def get_ranking(name):
    global all_rankings

    if name not in all_rankings:
        raise Error('Json not loaded')
    return all_rankings[name]

def choose_ranking(ranking):
    a = random.choice(ranking.entries)
    b = random.choice([e for e in ranking.entries if e != a])

    print(f'A: {a["display_name"]}')
    print(f'B: {b["display_name"]}')

    choice_made = None

    while choice_made is None:

        choice_made = input('Make a choice, "A", "B" or "=": ')

        if re.match('^[A=B]$', choice_made):
            choice_comparator = {'A': '>', '=': '=', 'B': '<'}[choice_made]

            ranking.add_comparison(f"{a['_id']}{choice_comparator}{b['_id']}")

        else:
            choice_made = None

def main():
    films = load_json('json/films4.json')

    choose = True
    while choose:
        choose_ranking(films)
        choose = 'y' in input('Continue? (y/n) ')

    print(list(films.calculate_rank()))

    save_json('films', 'json/films5.json')

if __name__ == '__main__':
    main()
