class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, recipe_type,
                 ingredients, description=None):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.recipe_type = recipe_type
        self.ingredients = ingredients
        self.description = description

    def __str__(self):
        text = f'''- Recipe: {self.name}
- Cooking level: {self.cooking_lvl}
- Cooking time: {self.cooking_time}
- Recipe type: {self.recipe_type}
- Ingredients: {' '.join(self.ingredients)}
- Description: {self.description}'''
        return text

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("recipe name must be a string")
        self._name = name

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, cooking_lvl):
        if not isinstance(cooking_lvl, int):
            raise TypeError("cooking level must be an integer")
        elif not (1 <= cooking_lvl <= 5):
            raise ValueError("cooking level must be an integer from 1 to 5")
        self._cooking_lvl = cooking_lvl

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, cooking_time):
        if not isinstance(cooking_time, int):
            raise TypeError("cooking time must be an integer")
        elif not cooking_time > 0:
            raise ValueError("cooking time must be a positive integer \
                             representing minutes")
        self._cooking_time = cooking_time

    @property
    def recipe_type(self):
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, recipe_type):
        if not isinstance(recipe_type, str):
            raise TypeError("recipe type must be a string")
        elif recipe_type not in ["entrante", "comida", "postre"]:
            raise ValueError("recipe type must be one of those: \
                             'entrante', 'comida' or 'postre'")
        self._recipe_type = recipe_type

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise TypeError("ingredients must be a list")
        elif len(ingredients) < 1 or not all(isinstance(item, str) for item in ingredients):
            raise TypeError("ingredients must be a list of strings \
                            containing the ingredient names")
        self._ingredients = ingredients

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if description and not isinstance(description, str):
            raise TypeError("description is optional but it must be a string")
        self._description = description
