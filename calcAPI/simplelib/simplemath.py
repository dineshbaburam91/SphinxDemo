""" Simple programming in the mathematics """

class Mathematics(object):
    """ Doing simple operation in mathematics """
    def __init__(self, a, b, c):
        """Create a add, sub, mul, div

        Raises 'ValueError' if it is negative

        """
        self.a, self.b, self.c = float(a), float(b), float(c) 
        if any ( s<=0 for s in (a, b, c) ):
            raise ValueError('value must be positive')
    
    def add(self):
       """Return addition of three numbers"""
       return self.a + self.b + self.c

    def sub(self):
        """Return subtraction of two numbers"""
        return self.a - self.b

    def mul(self):
        """Return multiply of three numbers"""
        return self.a * self.b * self.c

    def div(self):
        """Return Division of two numbers"""
        return self.a / self.b     
