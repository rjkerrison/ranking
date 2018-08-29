import enum
import hashlib
import re
import json
from .io import get_input

class Encoder(json.JSONEncoder):
    def default(self, obj):
        return obj

class Ordering(enum.Enum):
    OneBeatsTwo = -1
    OnAPar = 0
    TwoBeatsOne = 1

class Ranking():
    def __init__(self, name, details, entries, rank_data, display_name = None):
        self.name = name
        self.details = details
        self.entries = entries
        self.rank_data = rank_data
        self.display_name = display_name or '{name}'

        self._initialise_rank_data()
        self._set_display_names()

    def _initialise_rank_data(self):
        for entry in self.entries:
            if '_id' not in entry:
                entry['_id'] = self._generate_unique_id(entry)

        self.rank_data = self.rank_data or []
        return self.rank_data

    def _generate_unique_id(self, entry):
        json_to_encode = json.dumps(entry)
        encoded_json = json_to_encode.encode('ascii')
        return hashlib.sha256(encoded_json).hexdigest()

    def _set_display_names(self):
        for entry in self.entries:
            entry['display_name'] = self.display_name.format(**entry)

    def calculate_rank(self):
        entry_scores = {entry['_id']:0 for entry in self.entries}

        for comparison in self.rank_data:
            id1, id2, ordering = self.__parse_comparison(comparison)

            if ordering == Ordering.OneBeatsTwo:
                entry_scores[id1] += 2
                entry_scores[id2] += -1

            if ordering == Ordering.OnAPar:
                entry_scores[id1] += 1
                entry_scores[id2] += 1

            if ordering == Ordering.TwoBeatsOne:
                entry_scores[id1] += -1
                entry_scores[id2] += 2

        ranked_entries = sorted(
            self.entries,
            key=lambda x: entry_scores[x['_id']],
            reverse=True)

        for entry in ranked_entries:
            print(f"{entry['name']:30}{entry_scores[entry['_id']]}")

    def __parse_comparison(self, comparison):
        match = re.match(r'^([0-9a-f]+)([<=>])([0-9a-f]+)$', comparison)

        id1 = self.__get_entry_by_partial_id(match.group(1))
        id2 = self.__get_entry_by_partial_id(match.group(3))
        ordering = self.__get_ordering_from_connector(match.group(2))

        return id1, id2, ordering

    def add_comparison(self, comparison=None):
        if comparison is None:
            comparison = self.__add_comparison_dialog() 
        self.rank_data.append(comparison)

    def add_entry(self):
        new_entry = self.__add_entry_dialog()
        new_entry['_id'] = self._generate_unique_id(new_entry)
        self.entries.append(new_entry)

    def find_entry(self, search_term, search_field=None):
        matched_entries = [f for f in self.entries if self.__entry_matches(f, search_term, search_field)]

        number_matches = len(matched_entries)

        if number_matches == 0:
            raise Exception('No matches found.')
        if number_matches == 1:
            return matched_entries[0]

        for i in range(0, number_matches):
            print(f'{i}: {matched_entries[i]}')

        chosen_index = None

        while chosen_index is None:
            try:
                input_choice = int(get_input('Choose one. Give the index: '))
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

    def __add_comparison_dialog(self):
        for entry in self.entries:
            print(f"{entry['_id']}: {entry['name']}")

        value = get_input('Give a comparison like "a234<b567" or "c123=d314": ')

        match = re.match(r'^([0-9a-f]+)([<=>])([0-9a-f]+)$', value)

        if match:
            return value
        raise Exception('Invalid comparison format')

    def __get_ordering_from_connector(self, connector):
        if connector == '>':
            return Ordering.OneBeatsTwo
        if connector == '=':
            return Ordering.OnAPar
        if connector == '<':
            return Ordering.TwoBeatsOne

    def __get_entry_by_partial_id(self, partial_id):
        matched_entries = [entry['_id'] for entry in self.entries if partial_id in entry['_id']]
        if len(matched_entries) == 1:
            return matched_entries[0]
        raise Exception(f"{partial_id} matched {len(matched_entries)} entries.")

    def __add_entry_dialog(self):
        entry_dictionary = {}

        for key, description in self.details.items():
            value = get_input(description + ': ')
            entry_dictionary[key] = value

        return entry_dictionary
