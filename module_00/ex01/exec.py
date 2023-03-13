import sys

string = ' '.join(sys.argv[1:])
inv_string_swapcase = string[::-1].swapcase()

print(inv_string_swapcase)
