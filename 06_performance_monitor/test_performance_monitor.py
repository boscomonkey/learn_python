#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- python test_performance_monitor.py -v

# # Topics
#
# * stubs
# * lambdas
# * invocation
#
# # Performance Monitor
#
# This is (a stripped down version of) an actual useful concept: a function that runs a block of code and then tells you how long it took to run.

from performance_monitor import measure
import random
import time

class FakeTime:
    eleven_am = time.strptime('Thu Mar  8 11:00:00 2018')

    def __init__(self):
        self.epoch_seconds = time.mktime(FakeTime.eleven_am)

    def increment(self, seconds):
        self.epoch_seconds += seconds

    def time(self):
        return self.epoch_seconds

def testFakeTime(fn):
    """
    >>> measure(lambda: None) < 0.1	# takes about 0 seconds to run an empty block
    True

    >>> testFakeTime(lambda tm: None)	# takes exactly 0 seconds to run an empty block (with stubs)
    0.0

    >>> elapsed = measure(lambda: time.sleep(1))
    >>> elapsed > 1 and elapsed < 1.1	# takes a little over 1 second to run a block that sleeps for 1 second
    True

    >>> testFakeTime(lambda tm: tm.increment(60))	# takes exactly 1 second to run a block that sleeps for 1 second (with stubs)
    60.0
    """
    fake = FakeTime()
    saved_time, time.time = time.time, fake.time
    diff = measure(lambda: fn(fake))
    time.time = saved_time
    return diff

def testMultiple(times):
    """
    >>> testMultiple(4)	# runs a block N times
    4
    """
    class Counter:
        def __init__(self):
            self.value = 0
        def increment(self, amount=1):
            self.value += amount
    cc = Counter()
    measure(lambda: cc.increment(), times)
    return cc.value

def testMultipleAverages():
    """
    >>> testMultipleAverages()	# returns the average time, not the total time, when running multiple times
    6.5
    """
    run_times = [8,6,5,7]
    count = len(run_times)
    fake_time = FakeTime()
    saved_time, time.time = time.time, fake_time.time
    average_time = measure(lambda: fake_time.increment(run_times.pop()), count)
    time.time = saved_time
    return average_time

def testRandomAverages():
    """
    >>> testRandomAverages()	# returns the average time when running a random number of times for random lengths of time
    0.0
    """
    number_of_times = random.randrange(10) + 2

    fake_time = FakeTime()
    saved_time, time.time = time.time, fake_time.time
    average_time = measure(lambda: fake_time.increment(random.randrange(10)), number_of_times)
    time.time = saved_time

    return average_time - (fake_time.time() - FakeTime().time()) / number_of_times


if __name__ == '__main__':
    import doctest
    doctest.testmod()

