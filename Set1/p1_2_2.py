numbers = [2, 4, 9, 7, 8]
product = 1
counter = 0

if(len(numbers) == 0):
    out = 'None'
else:
    for index in numbers:
        product *= index
        counter += 1
out = product ** (1/counter)

print(out)