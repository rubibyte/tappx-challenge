class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    # @property
    # def name(self):
    #     return self.name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            print("AssertionError: recipe name must be a string.")
            # raise value error, assertion error, type error
            # exit()
        else:
            self.name = name

    @cooking_lvl.setter
    def cooking_lvl(self, cooking_lvl):
        if not isinstance(cooking_lvl, int) or cooking_lvl not in range(1, 6):
            print("AssertionError: cooking_lvl must be an integer from 1 to 5.")
        else:
            self.cooking_lvl = cooking_lvl

    @cooking_time.setter
    def cooking_time(self, cooking_time):
        if not isinstance(cooking_time, int) or cooking_time < 1:
            print("AssertionError: cooking_time must be an integer representing\
 minutes.")
        else:
            self.cooking_time = cooking_time

    @ingredients.setter
    def ingredients(self, ingredients):
        if not isinstance(ingredients, list) or \
        not all(isinstance(item, str) for item in ingredients):
            print("AssertionError: ingredients must be a list of \
 strings containing the ingredient names.")
        else:
            self.ingredients = ingredients

    @descriptioin.setter

    @recipe_type.setter
    def recipe_type(self, recipe_type):
        if not isinstance(recipe_type, str) or \
        recipe_type not in ["entrante", "comida", "postre"]:
            print("AssertionError: recipe_type must be on of \
those strings: 'entrante', 'comida' o 'postre'.")

