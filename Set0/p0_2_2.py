a = 8
b = 3
c = 22
delta = (b ** 2) - (4 * a * c)
print(delta)

if(delta != 0):
    firstRoot = (-b + (delta ** 0.5)) / (2 * a)
    secondRoot = (-b - (delta ** 0.5)) / (2 * a)
    out = (firstRoot, secondRoot)
else:
    out = (-b + (delta ** 0.5)) / 2 * a

print(out)