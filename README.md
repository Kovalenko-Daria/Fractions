# Fractions

## About
A custom implementation of a class for working with fractions, which allows you to perform various mathematical and comparison operations with them, provided that the input data is verified.
***

## Functionality
Possible actions with the class Fraction:

1) Fraction initiation
Object of Fraction class can be created from:
    * integer
    * float the number of decimal places of which doesn't not exceed 5
    * string 'int1/int2', where int1 is numerator and int2 is denominator
    * list [int1, int2], where int1 is numerator and int2 is denominator
    * tuple (int1, int2), where int1 is numerator and int2 is denominator
If you try to pass a different value to the class constructor, an error will be raised. It is also checked that the denominator is not equal to 0.
***

2) Fraction reduction
The fraction is always stored in reduced form. This is done using function `def reduce_fraction(num, den)` that can be accessed from the outside to reduce two numbers as `Fraction.reduce_fraction(num, den)`
***

3) Setting the value of the numerator and denominator
The attributes of the class that store the values of the numerator and denominator are private, so as not to violate the logic of the class and create erroneous fractions. That is why there are methods `def set_num(self, num)` and `def set_num(self, num)` by which you can change the values of the numerator and denominator, respectively. It is worth noting that when trying to set the denominator value to 0, an error will be raised.
***

4) Return the value of the numerator and denominator
To view the values of private attributes responsible for storing the numerator and denominator, methods `def get_num(self, num)` and `def get_num(self, num)`are implemented, respectively. Note: if the fraction is negative, then the numerator value will be returned negative, but the denominator will always be positive.
There is also defined a magic method `__str__` for beautifully displaying fractions.
***

5) Converting fractions to numeric data types
Fraction class objects can be converted to int, float and bool data types using the so-called functions.
***

6) Comparing fractions with valid data types
Fractions can be compared with Fractions and all types which are appropriate for converting to Fractions (look at 1)) using operators `==`, `!=`, `>`, `<`, `>=`, `<=`.
***

7) Mathematical operations between fractions and valid data types
Fractions can be calculated with Fractions and all types which are appropriate for converting to Fractions (look at 1)) using operators `+`, `+=`, `-` (unary and binary), `-=`, `*`, `*=`, `/`, `/=`, `**`, `**=` (exponent can be only a non-negative integer, otherwise an error will be raised). There is also implemented a special method to inverse fraction `def inverse_fraction(fraction)` and `abs` function.