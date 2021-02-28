_dictionary_ = {
    "brand": "Ford",
    "model": "Mustang",
}

def swap(d, k1, k2):
    temporary_variable = d[k1]
    d[k1] = d[k2]
    d[k2] = temporary_variable
    return None
