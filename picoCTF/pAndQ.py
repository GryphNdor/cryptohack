import math

def egcd(a, b):
  x,y, u,v = 0,1, 1,0
  while a != 0:
      q, r = b//a, b%a
      m, n = x-u*q, y-v*q
      b,a, x,y, u,v = a,r, u,v, m,n
      gcd = b
  return gcd, x, y

def main():
  p = 650809615742055581459820253356987396346063
  q = 2434792384523484381583634042478415057961
  e = 65537
  ct = 964354128913912393938480857590969826308054462950561875638492039363373779803642185

  n = p*q

  phi = (p - 1)*(q - 1)

  # Compute modular inverse of e
  gcd, a, b = egcd(e, phi)
  d = a

  # d = (1/math.e)%phi
  print( "n:  " + str(d) );

  # Decrypt ciphertext
  pt = pow(ct, d, n)
  print( "pt: " + str(pt) )

if __name__ == "__main__":
  main()

