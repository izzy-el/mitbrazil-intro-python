def f(x):
    return x * x * 3

def approx_derivative(f, x, delta = 10 ** -6):
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def approx_derivative_2(f, delta = 10 ** - 6):
    def _derivative_(x):
        return (f(x + delta) - f(x - delta)) / (2 * delta)
    return _derivative_

def approx_integral(f, lo, hi, num_regions):
    _sum_ = 0
    height = (hi - lo) / num_regions

    _sum_ += f(lo) / 2.0 + f(hi) / 2.0 #Adding the first and the last numbers before making it to the rule

    for i in range(1, num_regions):
        _sum_ += f(lo + i * height)

    return _sum_ * height

# print(approx_integral(f, 1, 5, 2))
