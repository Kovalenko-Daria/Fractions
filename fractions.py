class Fraction:

    def __init__(self, *args):
        if isinstance(args[0], str) and '/' in args[0]:
            self.num, self.den = [int(i) for i in args[0].split('/')]
        elif len(args) == 1:
            self.num, self.den = int(args[0]), 1 
        else:
            self.num, self.den = args[0], args[1]
        self.zn = 1
        self._sokr()
    
    def _sokr(self):
        self.zn = (-1 if self.zn * self.num * self.den < 0 else 1)
        self.num, self.den = abs(self.num), abs(self.den)
        _n = _gcd(self.num, self.den)
        self.num, self.den = self.num // _n, self.den // _n
    
    def numerator(self, *args):
        if len(args) == 0:
            return self.num
        self.num = args[0]
        self._sokr()
    
    def denominator(self, *args):
        if len(args) == 0:
            return self.den
        self.den = args[0]
        self._sokr()
    
    def __str__(self):
        return f"{self.zn * abs(self.num)}/{abs(self.den)}"
    
    def __repr__(self):
        return f"Fraction('{self.zn * abs(self.num)}/{abs(self.den)}')"
    
    def __neg__(self):
        return Fraction(-1 * self.zn * self.num, self.den)
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return Fraction(self.zn * self.num * _mn1 + other.zn * other.num * _mn2,
                        _new_den)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return Fraction(self.zn * self.num * _mn1 - other.zn * other.num * _mn2,
                        _new_den)
    
    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        self.num, self.den = (self.zn * self.num * _mn1 +
                              other.zn * other.num * _mn2), _new_den
        self.zn = 1
        self._sokr()
        return self
    
    def __isub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        self.num, self.den = (self.zn * self.num * _mn1 -
                              other.zn * other.num * _mn2), _new_den
        self.zn = 1
        self._sokr()
        return self
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.zn * self.num * other.zn * other.num, self.den * other.den)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        other = other.reverse()
        return Fraction(self.zn * self.num * other.zn * other.num, self.den * other.den)
    
    def __imul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        self.num, self.den = self.zn * self.num * other.zn * other.num, self.den * other.den
        self.zn = 1
        self._sokr()
        return self
    
    def __itruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        other = other.reverse()
        self.num, self.den = self.zn * self.num * other.zn * other.num, self.den * other.den
        self.zn = 1
        self._sokr()
        return self
    
    def reverse(self):
        return Fraction(self.zn * self.den, self.num)
    
    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return self.zn * self.num * _mn1 > other.zn * other.num * _mn2
    
    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return self.zn * self.num * _mn1 >= other.zn * other.num * _mn2
    
    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return self.zn * self.num * _mn1 < other.zn * other.num * _mn2
    
    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return self.zn * self.num * _mn1 <= other.zn * other.num * _mn2
    
    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return self.zn * self.num * _mn1 == other.zn * other.num * _mn2
    
    def __ne__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return self.zn * self.num * _mn1 != other.zn * other.num * _mn2
    
    def __radd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return Fraction(self.zn * self.num * _mn1 + other.zn * other.num * _mn2,
                        _new_den)
    
    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        _new_den = self.den * other.den // _gcd(self.den, other.den)
        _mn1, _mn2 = _new_den // self.den, _new_den // other.den
        return Fraction(other.zn * other.num * _mn2 - self.zn * self.num * _mn1,
                        _new_den)
    
    def __rmul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.zn * self.num * other.zn * other.num, self.den * other.den)
    
    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.zn * self.den * other.zn * other.num, self.num * other.den)


def _gcd(_a, _b):
    while _a != _b:
        if _a > _b:
            _a -= _b
        else:
            _b -= _a
    return _a