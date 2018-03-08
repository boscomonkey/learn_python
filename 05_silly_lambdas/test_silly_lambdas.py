#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- python test_silly_lambdas.py -v

from silly_lambdas import reverser, adder, repeater

def test01Reverser():
    """
    >>> reverser(lambda: 'hello')	# reverses the string returned by the default block
    'olleh'
    >>> reverser(lambda: 'hello dolly')	# reverses each word in the string returned by the default block
    'olleh yllod'
    """
    pass

def test02Adder():
    """
    >>> adder(lambda: 5)	# adds one to the value returned by the default block
    6
    >>> adder(lambda: 5, 3)	# adds 3 to the value returned by the default block
    8
    """
    pass

def testRepeater(num=1):
    """
    >>> testRepeater()	# executes the default block
    667
    >>> testRepeater(3)	# executes the default block 3 times
    669
    >>> testRepeater(10)	# executes the default block 10 times
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
