import re

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return int(n1 / n2)
def multiply(n1, n2):
    return n1 * n2

number_dictionary = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}
operation_dictionary = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply,
}

def check_expression(expression):
    try:
        if len(expression) < 3:
            raise (ValueError())
    except ValueError:
        print("You must have 2 operands and 1 operation")
        return False

    try:
        if ' ' in expression:
            raise (ValueError())
        for letter in expression:
            if letter not in number_dictionary and letter not in operation_dictionary:
                raise (KeyError())

    except ValueError:
        print("You can't have spaces in your expression.")
        return False
    except KeyError:
        print("It's not a mathematical expression(Incorrect arguments or operation).")
        return False

    try:
        #optional(never used)
        counter = 0
        for letter in expression:
            if letter in operation_dictionary:
                counter += 1
            elif letter in number_dictionary:
                counter = 0
            elif counter > 1:
                raise (ValueError())
    except ValueError:
        print("You can't write more than 1 operation symbol in a row")
        return False

    try:
        counter = 0
        for letter in expression:
            if letter in operation_dictionary:
                counter += 1
        if counter > 1:
            raise (ValueError())
        if expression[-1] in operation_dictionary or expression[0] in operation_dictionary:
            raise (KeyError())
    except ValueError:
        print("You can have only 1 operation symbol at a time")
        return False
    except KeyError:
        #optianal(never used)
        print("You can't start with math operation symbol or end with it")
        return False

    try:
        counter = 0
        for letter in expression:
            if letter in number_dictionary:
                counter += 1
            elif letter in operation_dictionary:
                counter = 0
            if counter == 2 and letter != '0':
                raise (ValueError())
            if counter == 3:
                raise (ValueError())
    except ValueError:
        print("You can use numbers only between 1 and 10")
        return False
    return True
def check_expression_with_regular_exp(expression):
    #optional))))
    try:
        pattern = r'^([1-9]|10)([+\-*/])([1-9]|10)$'
        if re.match(pattern, expression):
            return True
        else:
            raise (ValueError())
    except ValueError:
        print("Your expression doesn't match calc conditions")

def main():
    expression = input("Write down your expression: ")
    if check_expression(expression):
        operand_1 = ''
        operand_2 = ''
        operation = ''
        for letter in expression:
            if letter not in operation_dictionary and operation == '':
                operand_1 += letter
            elif letter in operation_dictionary:
                operation = letter
            elif letter not in operation_dictionary and operation != '':
                operand_2 += letter
        result = operation_dictionary[operation](int(operand_1), int(operand_2))
        print(result)

main()













