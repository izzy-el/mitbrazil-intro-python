interest_rate = 0.5
balance = 1000
auxiliary = 0
out = 0

if(interest_rate == 0):
    out = "NEVER"
else:
    while(auxiliary < balance * 2):
        auxiliary += balance * (1 + interest_rate) ** out
        out += 1

print(out)
