#Batyrkhan Abukhanov 201886883
def gcd(n1, n2) :
    if n1 == 0 and n2 == 0 :
        raise ArithmeticError("gcd(0,0) does not exist")
    if n1 == 0 :
        return n2
    if n2 == 0 :
        return n1

    while True:
        r = n1 % n2
        if not r:
            break
        n1 = n2
        n2 = r
    return n2


from numbers import *

class Rational(Number) :
    def __init__(self, num, denom = 1) :
        if not isinstance(num, Integral) :
            raise TypeError("Rational: numerator {} must be Integral". format(num))

        if not isinstance(denom, Integral) :
            raise TypeError("Rational: denominator {} must be Integral". format(denom))

        self.num = num
        self.denom = denom

        self.normalize()

    def normalize(self) :
        if self.denom == 0 :
            raise ArithmeticError("denom cannot be zero")

        if self.denom < 0 :
            self.num = self.num * (-1)
            self.denom = self.denom * (-1)

        tmp_gcd = gcd(self.num, self.denom)
        self.num = self.num // tmp_gcd
        self.denom = self.denom // tmp_gcd

    def __repr__(self) :
        return "Rational( {}, {} )".format(self.num, self.denom)

    def __str__(self) :
        if self.denom == 1 :
            return "{}".format(self.num)
        else :
            return "{} / {}".format(self.num, self.denom)

    def __neg__(self) :
        return Rational(-self.num, self.denom)

    def __add__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        return Rational( (self.num * other.denom + self.denom * other.num), (self.denom * other.denom) )

    def __sub__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        return Rational( (self.num * other.denom - self.denom * other.num), (self.denom * other.denom) )

    def __radd__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        return Rational( (self.num * other.denom + self.denom * other.num), (self.denom * other.denom) )

    def __rsub__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        return Rational( (self.denom * other.num - self.num * other.denom), (self.denom * other.denom) )

    def __mul__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        return Rational((self.num * other.num), (self.denom * other.denom))

    def __truediv__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        return Rational((self.num * other.denom), (self.denom * other.num))

    def __rmul__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        return Rational((self.num * other.num), (self.denom * other.denom))

    def __rtruediv__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        return Rational((other.num * self.denom), (other.denom * self.num))

    def __eq__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        if self.num == other.num and self.denom == other.denom :
            return True
        else :
            return False

    def __ne__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)
        if self.num == other.num and self.denom == other.denom :
            return False
        else :
            return True

    def __lt__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)

        if self.num * other.denom < other.num * self.denom :
            return True
        else :
            return False

    def __gt__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)

        if self.num * other.denom > other.num * self.denom :
            return True
        else :
            return False

    def __le__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)

        if self.num * other.denom > other.num * self.denom :
            return False
        else :
            return True

    def __ge__(self, other) :
        if not isinstance(other, Rational) :
            other = Rational(other)

        if self.num * other.denom < other.num * self.denom :
            return False
        else :
            return True



    def getfloat( self ) :
        return self. num / self. denom

def summation( it, x ) :
    sum = 0
    xpow = 1
    for coeff in it :
        sum += xpow * coeff
        xpow *= x
    return sum