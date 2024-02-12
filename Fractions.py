class Fraction:

    @staticmethod
    def validate_fraction(fraction):
        
        if not (isinstance(fraction, int) or isinstance(fraction, float) or isinstance(fraction, str) or isinstance(fraction, list) or isinstance(fraction, tuple)):
            raise TypeError("Fraction can be set only as float, int, string 'int1/int2', list [int1, int2] or tuple (int1, int2), where int1 is numerator and int2 is denominator")
        
        if isinstance(fraction, tuple) or isinstance(fraction, list):
            if len(fraction) != 2 or not isinstance(fraction[0], int) or not isinstance(fraction[1], int):
                raise TypeError("When Fraction is set as list or tuple, it should be [int1, int2] or (int1, int2) respectively, where int1 is numerator and int2 is denominator")
            if fraction[1] == 0:
                raise ZeroDivisionError("0 cannot be a denominator")
        
        if isinstance(fraction, str):
            try:
                f = [int(i) for i in fraction.split('/')]
                if len(f) != 2:
                    raise ValueError
                if f[1] == 0:
                    raise ZeroDivisionError("0 cannot be a denominator")
            except ValueError or IndexError:
                raise TypeError("When Fraction is set as str, it should be 'int1/int2', where int1 is numerator and int2 is denominator")
        
        if isinstance(fraction, float):
            f = str(fraction).split('.')[1]
            if len(f) > 5:
                raise TypeError("When Fraction is set as float, the number of decimal places should not exceed 5")
    
    @staticmethod
    def validate_num_den(arg, den=False):
        if not isinstance(arg, int):
            raise TypeError("numerator and denominator can be set only as integer")
        if den and arg == 0:
            raise ZeroDivisionError("0 cannot be a denominator")  
        
    @staticmethod
    def validate_for_gcd(num1, num2):
        if not (isinstance(num1, int) and isinstance(num2, int)):
            raise ValueError("function takes only integers except 0")

    @staticmethod
    def validate_for_inverse(fraction):
        if not isinstance(fraction, Fraction):
            raise TypeError("function takes only Fraction")

    def __convert_fraction(self, fraction):

        if isinstance(fraction, list) or isinstance(fraction, tuple):
            num, den = fraction

        elif isinstance(fraction, str):
            num, den = [int(i) for i in fraction.split('/')]
        
        elif isinstance(fraction, int):
            num, den = fraction, 1

        else:
            f = 10**len(str(fraction).split('.')[1])
            num, den = int(fraction * f), f

        sign = 1 if num * den >= 0 else -1
        num, den = Fraction.reduce_fraction(abs(num), abs(den))
        return sign, num, den
    
    @staticmethod
    def gcd(num1, num2):
        Fraction.validate_for_gcd(num1, num2)
        num1, num2 = abs(num1), abs(num2)
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 %= num2
            else:
                num2 %= num1
        return 1 if num1 == num2 else max(num1, num2)

    @staticmethod
    def reduce_fraction(num, den):
        if den == 0:
            raise ZeroDivisionError("0 cannot be a denominator")
        gcd = Fraction.gcd(num, den)
        if num == 0 and den < 0:
            den *= -1
        return num // gcd, den // gcd

    @staticmethod
    def inverse_fraction(fraction):
        num, den = fraction.get_num(), fraction.get_den()
        if num != 0:
            new_fraction = Fraction((den, num))
        else:
            new_fraction = Fraction(0)
        return new_fraction

    def __init__(self, fraction):
        self.validate_fraction(fraction)
        self.__sign, self.__num, self.__den = self.__convert_fraction(fraction)
    
    def __str__(self):
        s = '' if self.__sign == 1 else '-'
        if self.__num == 0:
            return '0'
        if self.__num == self.__den:
            return f'{s}1'
        if self.__den == 1:
            return f'{s}{self.__num}'
        if self.__num > self.__den:
            return f'{s}{self.__num}/{self.__den} or {s}{self.__num // self.__den} {self.__num % self.__den}/{self.__den}'
        return f'{s}{self.__num}/{self.__den}'
    
    def get_num(self):
        return self.__sign * self.__num

    def get_den(self):
        return self.__den
    
    def set_num(self, num):
        self.validate_num_den(num)
        if num >= 0:
            self.__sign = 1
        else:
            self.__sign = -1
        self.__num, self.__den = self.reduce_fraction(abs(num), self.__den)

    def set_den(self, den):
        self.validate_num_den(den, den=True)
        if den < 0:
            self.__sign = 1 if self.__num <= 0 else -1
        self.__num, self.__den = self.reduce_fraction(self.__num, abs(den))

    def __int__(self):
        return int(self.get_num() / self.get_den())

    def __float__(self):
        return  round(float(self.get_num() / self.get_den()), 5)

    def __bool__(self):
        return self.__num != 0

    def __abs__(self):
        return Fraction((self.__num, self.__den))
    
    def __eq__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return (self.get_num() == other.get_num() == 0 or
                (self.get_num() == other.get_num() and self.get_den() == other.get_den()))
    
    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.get_num() * other.get_den() < self.get_den() * other.get_num()
    
    def __gt__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.get_num() * other.get_den() > self.get_den() * other.get_num()
    
    def __le__(self, other):
        return self == other or self < other
    
    def __ge__(self, other):
        return self == other or self > other

    def __add__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction((self.get_num() * other.get_den() + other.get_num() * self.get_den(),
                         self.get_den() * other.get_den()))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction((self.get_num() * other.get_num(), 
                         self.get_den() * other.get_den()))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other    

    def __pow__(self, other):
        if not isinstance(other, int) or other < 0:
            raise ValueError("exponent should be non-negative integer")
        if other == 0:
            return Fraction(1)
        res_n = n = self.get_num()
        res_d = d = self.get_den()
        for _ in range(other - 1):
            res_n *= n
            res_d *= d
        return Fraction((res_n, res_d))
        
    def __ipow__(self, other):
        return self ** other

    def __sub__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction((self.get_num() * other.get_den() - other.get_num() * self.get_den(),
                         self.get_den() * other.get_den()))        

    def __rsub__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return other - self

    def __isub__(self, other):
        return self - other

    def __truediv__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction((self.get_num() * other.get_den(), 
                         self.get_den() * other.get_num()))

    def __rtruediv__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return other / self

    def __itruediv__(self, other):
        return self / other

    def __neg__(self):
        return Fraction((-1 * self.get_num(), self.get_den()))
