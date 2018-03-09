import time

class Timer:

    def __init__(self, starting_value=0):
        self.seconds = starting_value

    def time_string(self):
        gmt = time.gmtime(self.seconds)
        return time.strftime('%H:%M:%S', gmt)

