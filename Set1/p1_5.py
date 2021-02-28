size = 'medium'
toppings = ['cebola', 'abacaxi', 'bacon']
out = 0

if size == 'small':
    out = 14
elif size == 'medium':
    out = 16
elif size == 'large':
    out = 18
for index in range(len(toppings)):
    out += (12 + index + (len(toppings[index]))) * out / 100

if('bacon' in toppings or 'anchovas' in toppings):
    out *= 1.1
    
print(out)