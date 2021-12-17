import math
print(1%13)

# a**p === a % p
# pow(a,p-1) = 1 % 13
# a^(p-1) = 1 % 13
p = 13
print(math.pow(3, p-2) % p)