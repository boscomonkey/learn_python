import time

def measure(fn, repeat=1):
    before = time.time()
    for ii in range(repeat):
        fn()
    after = time.time()
    diff = after - before
    return diff / repeat
