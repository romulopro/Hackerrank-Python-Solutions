class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, n):
        return Complex(self.real + n.real, self.imaginary + n.imaginary)
    def __sub__(self, n):
        return Complex(self.real - n.real, self.imaginary - n.imaginary)
    def __mul__(self, n):
        return Complex((self.real * n.real) - (self.imaginary * n.imaginary), (self.real * n.imaginary) + (n.real*self.imaginary))
    def __truediv__(self, n):
        comp = (complex(self.real, self.imaginary) / complex(n.real, n.imaginary))
        return Complex(comp.real, comp.imag)
    def mod(self):
        modulo = (self.real**2 + self.imaginary**2)**0.5
        return("%.2f+0.00i" %modulo)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result