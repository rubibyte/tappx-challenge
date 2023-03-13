import sys


def operations(a, b):
    if b == 0:
        return print(f'''Sum:		{a + b}
Difference:	{a - b}
Product:	{a * b}
Quotient:	ERROR (division by zero)
Remainder:	ERROR (modulo by zero)''')
    else:
        return print(f'''Sum:		{a + b}
Difference:	{a - b}
Product:	{a * b}
Quotient:	{a / b}
Remainder:	{a % b}''')


argv = sys.argv

if len(argv) == 1:
    print('''Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3''')
elif len(argv) < 3:
    print("AssertionError: too few arguments")
elif len(argv) > 3:
    print("AssertionError: too many arguments")
elif not (argv[1].isdigit() and argv[2].isdigit()):
    print("AssertionError: only integers")
else:
    operations(int(argv[1]), int(argv[2]))
