import sys

argv = sys.argv[:]


def who_is(num):
    if num == 0:
        print("I'm Zero.")
    elif num % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")


if len(argv) > 2:
    print("AssertionError: more than one argument are provided")
elif len(argv) < 2:
    print("AssertionError: less than one argument are provided")
elif not argv[1].isdigit():
    print("AssertionError: argument is not an integer")
else:
    who_is(int(argv[1]))
