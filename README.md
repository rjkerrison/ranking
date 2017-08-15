# ranking
A suite for ranking anything

## Example usage

Let's say you want to rank your favourite form of pastas.

Provide ranking with an initial Json file like so:

    {
      "details": {
        "name": "The name of the pasta",
        "shape": "A description of the shape",
        "price": "The price of the pasta per kilogram"
      },
      "name": "pasta",
      "entries": []
    }
   
Save this to `json/pasta.json`.

You can now load this into the ranking using `load_json`,
which converts the json above into a `Ranking` object and stores it against the 
`Ranking`'s name, which above was given as `"pasta"`.

    >>> import rank
    >>> rank.load_json('json/pasta.json')

You can now manipulate the ranking data to use the `Ranking` class's methods.

    >>> pasta_ranking = rank.get_ranking('pasta')

### `add_entry`

`add_entry` runs through a dialog based upon the `"details"` dictionary in the Json.

    >>> pasta_ranking.add_entry()
    The name of the pasta: spaghetti
    The price of the pasta per kilogram: 0.60
    A description of the shape: long cylindrical strands
    >>> pasta_ranking.add_entry()
    The name of the pasta: penne
    The price of the pasta per kilogram: 0.80
    A description of the shape: hollow cylindrical tubes with obliquely angled open ends
    
### `find_entry`

`find_entry` takes first parameter `search_term` and an optional second parameter `search_field`.

With just the `search_term`, it checks all fields for a textual match.

    >>> spaghetti = pasta_ranking.find_entry('spag')
    >>> spaghetti['shape'] = 'like penne but longer, with a smaller radius, and without the hole'
    
Given more than one match, it will prompt for an index selection.

    >>> penne = pasta_ranking.find_entry('penne')
    0: {'name': 'spaghetti', 'price': '0.60', 'shape': 'like penne but longer, with a smaller radius, and without the hole'}
    1: {'name': 'penne', 'price': '0.80', 'shape': 'hollow cylindrical tubes with obliquely angled open ends'}
    Choose one. Give the index: 0
    
Given a `search_field`, it will only target that field.
    
    >>> penne = pasta_ranking.find_entry('penne', 'name')
    >>> penne
    {'name': 'penne', 'price': '0.80', 'shape': 'hollow cylindrical tubes with obliquely angled open ends'}
    >>> spaghetti
    {'name': 'spaghetti', 'price': '0.60', 'shape': 'like penne but longer, with a smaller radius, and without the hole'}
    
### `save_json`

If you're all happy and that, give it a `save_json`.
You can save it to another file, if you're so inclined.
    
    >>> rank.save_json('pasta', 'json/pasta2.json')
