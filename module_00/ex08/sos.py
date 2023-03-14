import sys


argv = sys.argv
morse_dictionary = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/'
}


def input_rules():
    print("Input must be alphnumeric and at least one argument.")


if len(argv) < 2:
    print("AssertionError: too few arguments.")
    input_rules()
elif not ' '.join(argv[1:]).replace(' ', '').isalnum():
    print("AssertionError: input is not alphanumeric.")
    input_rules()
else:
    morse_str = ''
    for letter in ' '.join(argv[1:]).upper():
        if not morse_str:
            morse_str += morse_dictionary[letter]
        else:
            morse_str += (' ' + morse_dictionary[letter])
    print(morse_str)
