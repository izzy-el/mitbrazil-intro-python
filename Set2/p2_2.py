def prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                return False
    return True

print(prime(71))