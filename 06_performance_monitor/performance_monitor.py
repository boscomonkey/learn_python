import time

def measure(fn, repeats=1):
    epoch_before = time.time()
    for ii in range(repeats):
        fn()
    epoch_after = time.time()

    num_secs = epoch_after - epoch_before
    return num_secs / repeats
