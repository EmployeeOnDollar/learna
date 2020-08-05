""" if __name__ == '__main__': is used for understanding code is run directly or imported.
    First run this code. Observe the console outputs.
    First meaningful line run first: shows how __name__ is defined
    Second meaningful line run: defines the function
    Third meaningful line: checks the definition of __name__ with if statement
    """
print(f'This will show current definition of __name__ (out of def): __name__ = {__name__}')


def meseeks():
    print("If you see this, __name__ equals to '__main__' ")


if __name__ == '__main__':
    meseeks()
else:
    print('What is __name__?')
