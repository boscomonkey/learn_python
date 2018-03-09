class Temperature:

    CELSIUS_SCALE = 'celsius_scale'
    FAHRENHEIT_SCALE = 'fahrenheit_scale'

    def ctof(degrees):
        return degrees * 9/5 + 32

    def ftoc(degrees):
        return (degrees - 32) * 5/9

    @classmethod
    def from_celsius(cls, c_degrees):
        return cls(c=c_degrees)

    @classmethod
    def from_fahrenheit(cls, f_degrees):
        return cls(f=f_degrees)

    def __init__(self, f=None, c=None):
        # prioritize C over F
        if c is not None:
            self.scale = Temperature.CELSIUS_SCALE
            self.degrees = c
        else:
            self.scale = Temperature.FAHRENHEIT_SCALE
            self.degrees = f

    def in_celsius(self):
        if self.scale == Temperature.CELSIUS_SCALE:
            return self.degrees
        else:
            return Temperature.ftoc(self.degrees)

    def in_fahrenheit(self):
        if self.scale == Temperature.FAHRENHEIT_SCALE:
            return self.degrees
        else:
            return Temperature.ctof(self.degrees)


class Celsius(Temperature):

    def __init__(self, c_degrees):
        super().__init__(c=c_degrees)


class Fahrenheit(Temperature):

    def __init__(self, f_degrees):
        super().__init__(f=f_degrees)



