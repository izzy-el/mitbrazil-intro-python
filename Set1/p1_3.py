dividend = 7
divisor = 2
result = 0

while(divisor * result < dividend):
    result += 1

out = (result - (result * divisor - dividend), result * divisor - dividend)

print(out)