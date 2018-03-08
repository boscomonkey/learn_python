import re

def adder(fn, increment=1):
    num = fn()
    return num + increment

def repeater(fn, count=1):
    for ii in range(count):
        fn()

def reverser(fn):
    msg = fn()
    arry = re.compile('\s+').split(msg)
    queue = []
    for word in arry:
        queue.append(reverse_word(word))
    return ' '.join(queue)

def reverse_word(word):
    return ''.join(reversed(word))

