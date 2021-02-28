kwh_used = 1000
out = 0

if(kwh_used < 500):
    out += 500 * 0.45
elif(kwh_used >= 500 and kwh_used < 1500):
    out += 500 * 0.45 + ((kwh_used - 500) * 0.74)
elif(kwh_used >= 1500 and kwh_used < 2500):
    out += 500 * 0.45 + ((kwh_used - 500) * 0.74) + ((kwh_used - 1500) * 1.25)
elif(kwh_used >= 2500):
    out += 500 * 0.45 + ((kwh_used - 500) * 0.74) + ((kwh_used - 1500) * 1.25) + ((kwh_used - 2500) * 2)
    
out += out * 0.2
print(out)