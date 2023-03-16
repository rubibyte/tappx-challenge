from datetime import date
from recipe import Recipe



class Book:
	def __init__(self, name):
		if not isinstance(name, str):
			raise TypeError("book name must be a string")
		self._name = name
		self._last_update = date.today().strftime("%d-%m-%Y")
		self._creation_date = date.today().strftime("%d-%m-%Y")
		self._recipes_list = dict(entrante = list(), comida = list(), postre = list())


	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		if not isinstance(name, str):
			raise TypeError("book name must be a string")
		self._name = name
		self._last_update = date.today().strftime("%d-%m-%Y")

	@property
	def last_update(self):
		return self._last_update

	@property
	def creation_date(self):
		return self._creation_date

	def add_recipe(self, recipe):
		if not isinstance(recipe, Recipe):
			raise TypeError("recipe must be of type Recipe")
		self._recipes_list[recipe.recipe_type].append(recipe)
		self._last_update = date.today().strftime("%d-%m-%Y")
		print(f"{recipe.name} added successfully to the list!")

	def get_recipes_by_types(self, recipe_type):
		if not isinstance(recipe_type, str):
			raise TypeError("recipe type must be a string")
		elif recipe_type not in ['entrante', 'comida', 'postre']:
			raise ValueError("recipe type must be one of those: 'entrante', \
'comida' or 'postre'")
		print(f"\nTo eat as {recipe_type}:\n")
		for recipe in self._recipes_list[recipe_type]:
			print(recipe)
			print()

	def get_recipe_by_name(self, name):
		if not isinstance(name, str):
			raise TypeError("recipe name must be a string")





# book = Book('recetario')

# # print(book.__dict__)

# book.add_recipe(Recipe('tarta', 3, 49, 'postre', ['harina', 'huevos'], 'mete todo al horno y espera'))

# # print(book.__dict__)

# book.add_recipe(Recipe('paella', 3, 9, 'comida', ['harina', 'huevos'], 'mete todo al horno y espera'))

# book.add_recipe(Recipe('pasta', 3, 49, 'postre', ['harina', 'huevos'], 'mete todo al horno y espera'))
# book.add_recipe(Recipe('alfajores', 3, 49, 'postre', ['harina', 'huevos'], 'mete todo al horno y espera'))

# # print(book.__dict__)

# book.get_recipes_by_types('postre')











