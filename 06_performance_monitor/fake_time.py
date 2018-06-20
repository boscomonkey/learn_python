# -*- coding: utf-8 -*-

import time

class FakeTime:
    eleven_am = time.strptime('Thu Mar  8 11:00:00 2018')

    def __init__(self):
        """Instantiates with some fake time.
        """
        self.epoch_seconds = time.mktime(FakeTime.eleven_am)

    def increment(self, seconds):
        """Increments internal timer by 'seconds'

        >>> ft = FakeTime()
        >>> start = ft.time()
        >>> ft.increment(666)
        >>> ft.time() - start
        666.0
        """
        self.epoch_seconds += seconds

    def time(self):
        """Returns number of seconds, à la time.time()

        >>> FakeTime().time() > 0
        True
        """
        return self.epoch_seconds


if __name__ == '__main__':
    import doctest
    doctest.testmod()

