#!/usr/bin/env python

# This driver is executable from the command line.  Use the Python
# "rerun" package to re-run the driver whenever files in this
# directory (and its recursive children) are changed or added.
#
#   rerun -v ./test_performance_monitor.py

import random
import time
import unittest
from counter import Counter
from fake_time import FakeTime
from performance_monitor import measure

class TestPerformanceMonitor(unittest.TestCase):

    DELTA = 0.01

    def test_010_empty_block(self):
        num_secs = measure(lambda: None)
        self.assertAlmostEqual(num_secs, 0,
                                   delta=type(self).DELTA,
                                   msg='takes about 0 seconds to run an empty block')

    def test_020_stubbed_block(self):
        elapsed = self.__measure_stubbed_time(lambda fake: None)
        self.assertEqual(elapsed, 0, 'takes exactly 0 seconds to run an empty block (with stubs)')

    def test_030_sleep_approx_1_second(self):
        elapsed = measure(lambda: time.sleep(1))
        self.assertAlmostEqual(elapsed, 1,
                                   delta=type(self).DELTA,
                                   msg='takes about 1 second to run a block that sleeps for 1 second')

    def test_040_sleep_exact_1_second(self):
        elapsed = self.__measure_stubbed_time(lambda fake: fake.increment(1))
        self.assertEqual(elapsed, 1, 'takes exactly 1 second to run a block that sleeps for 1 second (with stubs)')

    def test_050_runs_block_n_times(self):
        cc = Counter()
        self.assertEqual(cc.value, 0)
        measure(lambda: cc.increment(), 4)
        self.assertEqual(cc.value, 4, 'runs a block N times')

    def test_060_averages_run_time(self):
        run_times = [8,6,5,7]
        average_time = self.__measure_stubbed_time(lambda fake: fake.increment(run_times.pop()), len(run_times))
        self.assertEqual(average_time, 6.5, 'returns the average time, not the total time, when running multiple times')

    def test_070_averages_random_iterations(self):
        number_of_times = random.randrange(10) + 2
        fake_time = FakeTime()
        start_time = fake_time.time()

        stashed_fn, time.time = time.time, fake_time.time
        average_time = measure(lambda: fake_time.increment(random.randrange(10)), number_of_times)
        time.time = stashed_fn

        elapsed = fake_time.time() - start_time
        self.assertEqual(average_time, elapsed/number_of_times, 'returns the average time when running a random number of times for random lengths of time')

    ####
    #### internal
    ####

    def __measure_stubbed_time(self, fn, repeats=1):
        fake_time = FakeTime()
        stashed_fn, time.time = time.time, fake_time.time
        elapsed_time = measure(lambda: fn(fake_time), repeats)
        time.time = stashed_fn
        return elapsed_time


if __name__ == '__main__':
    unittest.main()
