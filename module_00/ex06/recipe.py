cookbook = {
    "bocadillo": {
        "ingredients": ["jamón", "pan", "queso", "tomate"],
        "meal": "almuerzo",
        "prep_time": 10
    },
    "tarta": {
        "ingredients": ["harina", "azucar", "huevos"],
        "meal": "postre",
        "prep_time": 60
    },
    "ensalada": {
        "ingredients": ["aguacate", "rúcula", "tomates", "espinacas"],
        "meal": "almuerzo",
        "prep_time": 15
    }
}


def print_recipes(dictionary):
    for key in dictionary.keys():
        print(key)


def print_recipe_details(recipe):
    if recipe not in cookbook.keys():
        return print("Sorry, this recipe does not exist")
    else:
        print(f'''Recipe for {recipe}:
    Ingredients list: {cookbook.get(recipe).get("ingredients")}
    To be eaten for {cookbook.get(recipe).get("meal")}.
    Takes {cookbook.get(recipe).get("prep_time")} minutes of cooking.''')


def delete_recipe(recipe):
    if recipe not in cookbook.keys():
        return print("Sorry, this recipe does not exist")
    else:
        cookbook.pop(recipe)


def add_recipe():
    name = input("Enter a name:\n")
    print("Enter ingredients:")
    ingredients = list(iter(input, ''))
    meal = input("Enter a meal type:\n")
    prep_time = input("Enter a preparation time:\n")
    cookbook[name] = \
        {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}
    print(f"\n{name} recipe added successfully!")


def print_available_options():
    print('''List of available options:
    1: Add a recipe
    2: Delete a recip
    3: Print a recipe
    4: Print the cookbook
    5: Quit
    ''', end='')


print("Welcome to the Python Cookbook !")
print_available_options()

quit = False

while not quit:
    option = input("\nPlease select an option:\n")
    print()
    if option == '1':
        add_recipe()
    elif option == '2':
        del_recipe = input("Enter recipe you want to delete:\n")
        print()
        delete_recipe(del_recipe)
        print(f"{del_recipe} recipe deleted successfully!")
    elif option == '3':
        name = input("Please enter a recipe name to get its details:\n")
        print()
        print_recipe_details(name)
    elif option == '4':
        print("The Cookbook contains this recipes:")
        print_recipes(cookbook)
    elif option == '5':
        print("Cookbook closed. Goodbye !")
        quit = True
    else:
        print("This is not a valid option. Valid options are numbers \
from 1 to 5.")
        print_available_options()
