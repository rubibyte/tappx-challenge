import random


print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
''')

secret_num = random.randint(1, 99)
quit = False
attempts = 0

while not quit:
    guess = input("What's your guess between 1 and 99?\n")
    attempts += 1
    if guess == 'exit':
        print("Goodbye!")
        quit = True
    elif not guess.isdigit():
        print("That's not a number.")
    elif int(guess) > secret_num:
        print("Too high!")
    elif int(guess) < secret_num:
        print("Too low!")
    else:
        if int(secret_num) == 42:
            print('''The answer to the ultimate question of life, \
the universe and everything is 42.''')
        if attempts == 1:
            print('''Congratulations! You got it on your first try!''')
        else:
            print(f'''Congratulations, you've got it!
You won in {attempts} attempts!''')
        quit = True
