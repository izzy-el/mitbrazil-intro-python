def square(num):
    return num * num

def fourth_power(num):
    return square(square(num))

# I did not want to use a library, so I came up with this way to figure it out if it is a perfect sqaure or not
def perfect_square(num):
    if ((num ** 0.5) % 1 == 0 or num == 0 or num == 1):
        return True
    else:
        return False
