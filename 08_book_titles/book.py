import re

class Book:

    def __init__(self):
        self._title = None

    def title(self):
        return self._title

    def setTitle(self, book_title):
        self._title = self.capitalize(book_title)

    ##
    ## internal
    ##

    exceptions = {
        'the', 'a', 'an',	# articles
        'and',				# conjunctions
        'in', 'of'			# prepositions
        }

    def capitalize(self, msg):
        words = re.compile('\s+').split(msg)
        buffer = []
        for token in words:
            if len(buffer) == 0:
                # always capitalize first word
                buffer.append(token.capitalize())
                continue

            if token in type(self).exceptions:
                buffer.append(token)
            else:
                buffer.append(token.capitalize())

        return ' '.join(buffer)

