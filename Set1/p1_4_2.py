poly = [2, 8]
const = 5
out = [const]

for index in range(len(poly)):
    out.append(poly[index] / (index + 1))

print(out)