def mdc(number_one, number_two):
    max_mdc = 1

    if number_one < number_two:
        for max in range(1, abs(number_one) + 1):
            if number_one % max == 0 and number_two % max == 0:
                max_mdc = max
    elif number_one >= number_two:
        for max in range(1, abs(number_two) + 1):
            if number_one % max == 0 and number_two % max == 0:
                max_mdc = max
    return max_mdc


class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def to_float(self):
        return self.numerator/self.denominator

    def reciprocal(self):
        return Rational(self.get_denominator(), self.get_numerator())

    def reduce(self):
        mdc_value = mdc(self.get_numerator(), self.get_denominator())
        return Rational(self.get_numerator() / mdc_value, self.get_denominator() / mdc_value)

    # Dunder methods

    def __add__(self, other):
        if isinstance(other, Rational):
            new_denominator = self.get_denominator() * other.get_denominator()
            return Rational(((new_denominator / self.get_denominator()) * self.get_numerator()) + ((new_denominator / other.get_denominator()) * other.get_numerator()), new_denominator).reduce()
        elif isinstance(other, int):
            return Rational(self.get_numerator() + self.get_denominator() * other, self.get_denominator()).reduce()
        elif isinstance(other, float):
            return self.to_float() + other
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.get_numerator() * other.get_numerator(), self.get_denominator() * other.get_denominator()).reduce()
        elif isinstance(other, int):
            return Rational(self.get_numerator() * other, self.get_denominator()).reduce()
        elif isinstance(other, float):
            return self.to_float() * other
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.get_numerator() * other.get_denominator(), self.get_denominator() * other.get_numerator()).reduce()
        elif isinstance(other, int):
            return Rational(self.get_numerator(), self.get_denominator() * other).reduce()
        elif isinstance(other, float):
            return self.to_float() / other
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational((self.get_numerator() * other.get_denominator() - self.get_denominator() * other.get_numerator()), (self.get_denominator() * other.get_denominator())).reduce()
        elif isinstance(other, int):
            return Rational(self.get_numerator() - self.get_denominator() * other, self.get_denominator()).reduce()
        elif isinstance(other, float):
            return self.to_float() - other
        else:
            return None
