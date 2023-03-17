import random


def generator(text, sep=' ', option=None):
    '''Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
option especifica si una acción se realizará sobre las sub-strings antes de \
ser producidas.
'''
    if not isinstance(text, str):
        raise TypeError("generator text input must be a string")
    elif not text.isprintable():
        raise ValueError("input text must not contain non-printable characters")
    if not isinstance(sep, str):
        raise TypeError("generator separator input must be a string")
    elif not sep.isprintable():
        raise ValueError("input separator must not contain non-printable characters")
    if option and not isinstance(option, str):
        raise TypeError("option input must be a string")
    if option and option not in ['shuffle', 'unique', 'ordered']:
        raise ValueError("option input must be one of those strings: \
'shuffle', 'unique' or 'ordered'")
    sub_strings = text.split(sep)
    if option == 'shuffle':
        def shuffle(x):
            return random.random()
        sub_strings.sort(key=shuffle)
    elif option == 'unique':
        sub_strings = list(dict.fromkeys(sub_strings))
    elif option == 'ordered':
        sub_strings.sort()
    return sub_strings
