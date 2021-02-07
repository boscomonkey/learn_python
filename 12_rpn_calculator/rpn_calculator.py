class RpnCalculator():

    def __init__(self):
        self.stack = []

    #
    # operators
    #

    def divide(self):
        self.binary_operate(lambda a, b: float(a) / float(b))

    def minus(self):
        self.binary_operate(lambda a, b: a - b)

    def plus(self):
        self.binary_operate(lambda a, b: a + b)

    def times(self):
        self.binary_operate(lambda a, b: a * b)

    #
    # actions
    #

    def push(self, num):
        self.stack.append(num)

    def value(self):
        num = self.stack[-1]
        return num

    #
    # internal
    #

    def binary_operate(self, fn):
        b = self.pop()
        a = self.pop()
        result = fn(a, b)
        self.push(result)

    def pop(self):
        try:
            num = self.stack.pop()
            return num
        except IndexError:
            raise CalculatorIsEmpty


class CalculatorIsEmpty(Exception):
    pass
