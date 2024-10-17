
def calculator():
    pass

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def product(a, b):
    return a * b

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("You can't divide by zero")
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculator()
