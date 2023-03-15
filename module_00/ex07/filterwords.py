import sys
import re


argv = sys.argv


def input_rules():
    print("Enter two arguments as input: a string and an integer.")


if len(argv) > 3:
    print("AssertionError: too many arguments.")
    input_rules()
elif len(argv) < 3:
    print("AssertionError: too few arguments.")
    input_rules()
elif not argv[2].isdigit():
    print("AssertionError: second argument is not an integer.")
    input_rules()
else:
    no_punct_str = re.sub(r'[^\w\s]', '', argv[1])
    # result = list()
    prueba = \
        list(word for word in no_punct_str.split() if len(word) > int(argv[2]))
    # for word in no_punct_str.split():
    #     if len(word) > int(argv[2]):
    #         result.append(word)
    # print(result)
    print(prueba)
