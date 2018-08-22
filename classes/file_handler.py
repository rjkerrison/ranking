import json
from .ranking import Ranking

def get_ranking_from_json(json_file):
    with open(json_file, 'r') as ranking_file:
        ranking_json = json.load(ranking_file)
        return Ranking(
            ranking_json['name'],
            ranking_json['details'],
            ranking_json['entries'],
            ranking_json['rank_data'] if 'rank_data' in ranking_json else None)

def save_ranking_to_json(ranking, json_file):
    with open(json_file, 'w') as ranking_file:
        json.dump(ranking.__dict__, ranking_file, indent=4)
