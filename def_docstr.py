# Def docstring

def say_hello():
    """Prints Hello Kokona!!!!"""
    print("Hello Coding Factory")


def main():
    say_hello()
    print(say_hello.__doc__)
    help(say_hello)


main()
