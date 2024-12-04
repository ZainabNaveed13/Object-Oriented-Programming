import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{self.real} + {self.imag}j"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __abs__(self):
        return math.sqrt(self.real*2 + self.imag*2)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Division by zero is undefined for complex numbers.")

        conjugate_denominator = ComplexNumber(other.real, -other.imag)
        numerator = self * conjugate_denominator
        denominator = other * conjugate_denominator

        return ComplexNumber(numerator.real / denominator.real, numerator.imag / denominator.real)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def modulus(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def argument(self):
        return math.atan2(self.imag, self.real)

    def to_polar_coordinates(self):
        r = self.modulus()
        theta = self.argument()
        return r, theta

    @classmethod
    def from_polar_coordinates(cls, r, theta):
        real_part = r * math.cos(theta)
        imag_part = r * math.sin(theta)
        return cls(real_part, imag_part)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __pow__(self, n):
        r, theta = self.to_polar_coordinates()
        result_r = r ** n
        result_theta = n * theta
        return ComplexNumber.from_polar_coordinates(result_r, result_theta)

    def sqrt(self):
        r, theta = self.to_polar_coordinates()
        result_r = math.sqrt(r)
        result_theta = theta / 2
        return ComplexNumber.from_polar_coordinates(result_r, result_theta)

    def log(self):
        r, theta = self.to_polar_coordinates()
        result_real = math.log(r)
        result_imag = theta
        return ComplexNumber(result_real, result_imag)

    def exp(self):
        result_real = math.exp(self.real) * math.cos(self.imag)
        result_imag = math.exp(self.real) * math.sin(self.imag)
        return ComplexNumber(result_real, result_imag)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def inverse(self):
        if self.real == 0 and self.imag == 0:
            raise ValueError("Inverse is undefined for complex number 0.")
        conjugate_denominator = self.conjugate()
        denominator = self * conjugate_denominator
        return conjugate_denominator / denominator


z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(1, -1)

# Perform operations
print("z1 =", z1)
print("z2 =", z2)
print("z1 + z2 =", z1 + z2)
print("z1 - z2 =", z1 - z2)
print("z1 * z2 =", z1 * z2)
print("|z1| =", abs(z1))
print("Conjugate of z1:", z1.conjugate())
print("Modulus of z1:", z1.modulus())
print("Argument of z1:", z1.argument())
print("Polar coordinates of z1:", z1.to_polar_coordinates())

z_polar = ComplexNumber.from_polar_coordinates(2, math.pi/4)
print("Complex number from polar coordinates:", z_polar)
