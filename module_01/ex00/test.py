from recipe import Recipe
from book import Book


tourte = Recipe('tarta', 1, 909040, 'entrante', ['harina', 'huevos', 'leche'], '')
print(tourte)

book = Book('recetario')

book.add_recipe(tourte)

print(book.__dict__)

book.add_recipe(Recipe('arroz con leche', 2, 49, 'postre', ['arroz', 'leche'], 'mete todo en una olla y espera'))

print(book.__dict__)

book.add_recipe(Recipe('paella', 3, 9, 'comida', ['arroz', 'cosas'], 'mete todo a la paella y espera'))
book.add_recipe(Recipe('pasta', 4, 49, 'postre', ['harina', 'huevos', 'agua', 'sal'], 'amasa la masa y espera'))
book.add_recipe(Recipe('alfajores', 5, 49, 'postre', ['dulce de leche', 'galleta'], 'galleta dulce de leche galleta'))

print(book.__dict__)

book.get_recipes_by_types('postre')

book.get_recipes_by_types('comida')

print(book._recipes_list)

book.get_recipe_by_name('tarta')
book.get_recipe_by_name('paella')

print(book.__dict__)
