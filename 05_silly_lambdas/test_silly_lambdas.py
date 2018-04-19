#!/usr/bin/env python

# This driver is executable from the command line.  Use the Python
# "rerun" package to re-run the driver whenever files in this
# directory (and its recursive children) are changed or added.
#
#   rerun -v './test_silly_lambdas.py -v'
#
# This test suite uses doctest instead of TestCase; thus, it needs a
# '-v' argument to indicate when all tests pass.


from silly_lambdas import reverser, adder, repeater

def test_10_reverser():
    """
    >>> reverser(lambda: 'hello')	# reverses the string returned by the default block
    'olleh'
    >>> reverser(lambda: 'hello dolly')	# reverses each word in the string returned by the default block
    'olleh yllod'
    """
    pass

def test_20_adder():
    """
    >>> adder(lambda: 5)	# adds one to the value returned by the default block
    6
    >>> adder(lambda: 5, 3)	# adds 3 to the value returned by the default block
    8
    """
    pass

def test_03_repeater(num=1):
    """
    >>> test_03_repeater()	# executes the default block
    667
    >>> test_03_repeater(3)	# executes the default block 3 times
    669
    >>> test_03_repeater(10)	# executes the default block 10 times
    676
    """
    class Counter:
        def incre(self):
            self.value += 1
    counter = Counter()
    counter.value = 666
    if num == 1:
        repeater(lambda: counter.incre())
    else:
        repeater(lambda: counter.incre(), num)
    return counter.value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
