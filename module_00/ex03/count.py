import string
import sys


def text_analyzer(input_str=None):
    '''
This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
    if not input_str:
        input_str = input("What is the text to analyze?\n")
    elif not isinstance(input_str, str):
        return print("AssertionError: argument is not a string")
    characters = 0
    upper_case = 0
    lower_case = 0
    punctuation = 0
    space = 0
    for i in input_str:
        if i.islower():
            lower_case += 1
        elif i.isupper():
            upper_case += 1
        elif i.isspace():
            space += 1
        elif i in string.punctuation:
            punctuation += 1
        characters += 1
    return print(f'''The text contains {characters} character(s):
- {upper_case} upper letter(s)
- {lower_case} lower letter(s)
- {punctuation} punctuation mark(s)
- {space} space(s)''')


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
    else:
        text_analyzer(sys.argv[1])
