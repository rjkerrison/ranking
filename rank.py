from data import ranking

all_rankings = {}

def load_json(json_file):
    rankin = ranking.get_ranking_from_json(json_file)
    all_rankings[rankin.name] = rankin

def save_json(ranking_name, json_file):
    ranking.save_ranking_to_json(all_rankings[ranking_name], json_file)

def get_ranking(name):
    global all_rankings

    if name not in all_rankings:
        raise Error('Json not loaded')
    return all_rankings[name]