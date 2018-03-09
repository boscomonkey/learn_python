class Friend():

    def greeting(self, buddy=None):
        if buddy is None:
            return 'Hello!'
        else:
            return 'Hello, %s!' % buddy

