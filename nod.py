import math

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))

mod = 0
i = 1

while i != 0:

    nod = mod
    mod = a % b
    celoe = a // b
    a = b
    b = mod
    if b == 0:
        break

print(nod)
print(math.gcd(a, b))