from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("book name must be a string")
        self.name = name
        self._last_update = datetime.now()
        self._creation_date = datetime.now()
        self._recipes_list = dict(entrante=dict(), comida=dict(), postre=dict())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("book name must be a string")
        self._name = name
        self._last_update = datetime.now()

    @property
    def last_update(self):
        return self._last_update

    @property
    def creation_date(self):
        return self._creation_date

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise TypeError("recipe must be of type Recipe")
        self._recipes_list[recipe.recipe_type][recipe.name] = recipe
        self._last_update = datetime.now()
        print(f"\n{recipe.name} added successfully to the list!")

    def get_recipes_by_types(self, recipe_type):
        if not isinstance(recipe_type, str):
            raise TypeError("recipe type must be a string")
        elif recipe_type not in ['entrante', 'comida', 'postre']:
            raise ValueError("recipe type must be one of those: 'entrante', \
'comida' or 'postre'")
        print(f"\nTo eat as {recipe_type}:\n")
        for recipe in self._recipes_list[recipe_type].values():
            print(recipe)
            print()

    def get_recipe_by_name(self, name):
        if not isinstance(name, str):
            raise TypeError("recipe name must be a string")
        for recipe_type in self._recipes_list.keys():
            recipe = self._recipes_list[recipe_type].get(name)
            if recipe:
                print()
                return print(recipe)
        raise ValueError("no recipe with this name in the book")
