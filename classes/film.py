import json

class Film():
    def __init__(self, film_dict):
        self.name = film_dict['name']
        self.director = film_dict['director']
        self.release_date = film_dict['release_date']

    def __getitem__(self, key):
        return self.__dict__[key]

    def __str__(self):
        return '{0}, directed by {1}'.format(
            self.name,
            self.director if type(self.director) is str else ', '.join(self.director)
        )

    def __repr__(self):
        return self.__str__().__repr__()

def get_film_dict_details():
    return {
        'name': 'The name of the film',
        'director': 'The director of the film',
        'release_date': 'The release date of the film'
    }

def get_films_from_json():
    with open('json/films.json', 'r') as films_file:
        films_json = json.load(films_file)
        return [Film(f) for f in films_json]

def save_films_to_json(films):
    with open('json/films.json', 'w') as films_file:
        json.dump([ob.__dict__ for ob in films], films_file, indent=4)
