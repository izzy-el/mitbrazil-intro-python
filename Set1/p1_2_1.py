numbers = []
sum = 0
counter = 0

if(len(numbers) == 0):
    out = None

else:
    for index in numbers:
        sum += index
        counter += 1

    out = sum / counter

print(out)