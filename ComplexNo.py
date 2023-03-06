class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return ComplexNumber(self.real+other.real, self.imag+other.imag)
    
    def __mul__(self, other):
        real = (self.real*other.real) - (self.imag*other.imag)
        imag = (self.real*other.imag) + (self.imag*other.real)
        return ComplexNumber(real, imag)
    
    def __str__(self):
        return f"{self.real}+{self.imag}i" if self.imag>=0 else f"{self.real}{self.imag}i"

# Example usage
x = ComplexNumber(1, 2)
y = ComplexNumber(3, 4)

print(x+y) # (1+2i) + (3+4i) = (4+6i)
print(x*y) # (1+2i) * (3+4i) = (-5+10i)
