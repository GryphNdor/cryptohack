def gcd(a,b):
  while(a != b):
    if(a>b):
      a = a-b
    else:
      b = b-a
  return a
  pass

# print(gfc(66528,52920))
print(gfc(26513,32321))
