import re

class Book:

    def __setattr__(self, name, value):
        """Override __setattr__ to handle capitalization of titles

        >>> b = Book()
        >>> b.age = 666
        >>> b.age
        666

        >>> b.author = 'george washington'
        >>> b.author
        'george washington'

        >>> b.title = 'little mermaid'
        >>> b.title
        'Little Mermaid'
        """
        if name == 'title':
            value = self.capitalize(value)

        super().__setattr__(name, value)

    ##
    ## internal
    ##

    DO_NOT_CAPITALIZE = {
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

            if token in type(self).DO_NOT_CAPITALIZE:
                buffer.append(token)
            else:
                buffer.append(token.capitalize())

        return ' '.join(buffer)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
