poly = [5, 0, 2, 4, 9, 7]
out = []

for index in range(1, len(poly)):
    out.append(poly[index] * index)

print(out)