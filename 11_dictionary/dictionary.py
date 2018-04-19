import re

class Dictionary():
    def __init__(self):
        self.hash = {}

    def add(self, key, definition=None):
        self.hash[key] = definition

    def entries(self):
        return self.hash

    def find(self, target):
        p = re.compile('^{}'.format(target))
        retval = {}
        for key, val in self.hash.items():
            if p.match(key):
                retval[key] = val
        return retval

    def includes(self, key):
        return key in self.hash

    def keywords(self):
        return sorted([key for key in self.hash])

    def printable(self):
        sorted_keys = self.keywords()
        lines = []
        for key in sorted_keys:
            val = self.hash[key]
            item = '[{}] "{}"'.format(key, val)
            lines.append(item)
        return '\n'.join(lines)
