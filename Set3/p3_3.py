base_dictionary = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4
}

def _function_(value):
    return value ** 3

def dictmap(d, f):
    for i in d:
        d[i] = f(d[i])
    print(d)
    return None
