def add(a, b):
    return a + b

def factorial(limit):
    accumulator = 1
    counter = 2
    while counter <= limit:
        accumulator *= counter
        counter += 1
    return accumulator

def multiply(*numbers):
    accumulator = 1
    for num in numbers:
        accumulator *= num
    return accumulator

def power(base, exponent):
    return base**exponent

def subtract(a, b):
    return a - b

def sum(arry):
    accumulator = 0
    for elt in arry:
        accumulator += elt
    return accumulator
