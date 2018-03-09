class Counter:

    def __init__(self):
        self.value = 0

    def increment(self, amount=1):
        """Increments internal counter value by amount (defaults to 1).

        >>> Counter().value
        0
        >>> Counter().increment(-1)
        -1
        >>> Counter().increment(666)
        666
        """
        self.value += amount
        return self.value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
