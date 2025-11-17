class Number:
    def __init__(self, a):
        self.a = a


"""
Rational Numbers

Only takes integers
"""
class Rational:
    # a and b should be integers
    def __init__(self, a, b):
        self.a = a
        if b == 0:
            raise ValueError("denominator cannot be 0")
        self.b = b

        self.reduce()

    def __add__(self, other):
        numerator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        return Rational(numerator, denominator).reduce()
    
    def __sub__(self, other):
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        return Rational(numerator, denominator).reduce()
    
    def __mul__(self, other):
        numerator = self.a * other.a
        denominator = self.b * other.b
        return Rational(numerator, denominator).reduce()
    
    def __truediv__(self, other):
        numerator = self.a * other.b
        denominator = self.b * other.a
        return Rational(numerator, denominator).reduce()
    
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False
    
    def __lt__(self, other):
        if self.a * other.b < other.a * self.b:
            return True
        return False
    
    def __gt__(self, other):
        if self.a * other.b > other.a * self.b:
            return True
        return False
    
    def __le__(self, other):
        if self.a * other.b <= other.a * self.b:
            return True
        return False
    
    def __ge__(self, other):
        if self.a * other.b >= other.a * self.b:
            return True
        return False
    
    def reduce(self):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        greatest_common_divisor = gcd(self.a, self.b)
        self.a //= greatest_common_divisor
        self.b //= greatest_common_divisor

        if self.b < 0:
            self.a *= -1
            self.b *= -1
        return self
    
    
    def print(self):
        if self.b == 1:
            print(f"{self.a}")
        else:
            print(f"{self.a}" + "/" + f"{self.b}")
    


"""
Complex Numbers

Only takes Rational Numbers
"""
class Complex:
    # a and b are Rational
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)
    
    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        return Complex(a, b)
    
    def __mul__(self, other):
        t1 = self.a * other.a
        t2 = self.a * other.b
        t3 = self.b * other.a
        t4 = (self.b * other.b) * -1
        return Complex(t1 + t4, t2 + t3)
    
    

"""
Square Root Numbers


"""
class Root:
    # x is the value under the radical
    # r is the root of the radical
    def __init__(self, x, r):
        self.x = x
        self.r = r

    # Apply Newton's method
    def val(self, l):
        pass

    def print(self):
        pass

    def __mul__(self, other):
        pass

    

