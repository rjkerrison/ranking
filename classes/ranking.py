import json

class Ranking():
    def __init__(self, name, details, entries):
        self.name = name
        self.details = details
        self.entries = entries

    def add_entry(self):
        new_entry = self.__add_entry_dialog()
        self.entries.append(new_entry)

    def find_entry(self, search_term, search_field=None):
        matched_entries = [f for f in self.entries if self.__entry_matches(f, search_term, search_field)]

        number_matches = len(matched_entries)

        if number_matches == 0:
            raise Error('No matches found.')
        if number_matches == 1:
            return matched_entries[0]

        for i in range(0, number_matches):
            print('{0}: {1}'.format(i, matched_entries[i]))

        chosen_index = None

        while chosen_index is None:
            try:
                input_choice = int(input('Choose one. Give the index: '))
                if input_choice in range(0, number_matches):
                    chosen_index = input_choice
            except:
                continue

        return matched_entries[chosen_index]

    def __entry_matches(self, entry, match_term, match_field):
        if match_field is None:
            for key, description in self.details.items():
                if match_term in entry[key]:
                    return True
                print(match_term, entry[key])
        else:
            if match_term in entry[match_field]:
                return True
        return False

    def __add_entry_dialog(self):
        entry_dictionary = {}

        for key, description in self.details.items():
            value = input(description + ': ')
            entry_dictionary[key] = value

        return entry_dictionary

def get_ranking_from_json(json_file):
    with open(json_file, 'r') as ranking_file:
        ranking_json = json.load(ranking_file)
        return Ranking(
            ranking_json['name'],
            ranking_json['details'],
            ranking_json['entries'])

def save_ranking_to_json(ranking, json_file):
    with open(json_file, 'w') as ranking_file:
        json.dump(ranking.__dict__, ranking_file, indent=4)