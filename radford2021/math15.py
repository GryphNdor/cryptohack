import math 
  
# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print (2, 
        n = n / 2)
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print(i, 
            n = n / i)
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print(n)
          
# Driver Program to test above function 
  
n = 287887932951506714823923619978330637542075563362520192925074220853614369212531809585138455408148165028422318526895440141888174958580813032513486078661141121114628763049545056489223834738859595774171434209353573364766713
primeFactors(n) 
