def f(x):
    return x * x * x

def g(x):
    return x + 15

def composite_result(f, g, x):
    return f(g(x))

def composite(f, g):
    def first_function(x):
        return f(g(x))
    return first_function

# print(composite(f, g)(4))