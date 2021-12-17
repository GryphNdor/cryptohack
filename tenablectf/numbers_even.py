def AreNumbersEven(numbers):
  bools = []
  for i in numbers:
    if(i % 2 == 0):
      bools.append(True)
    else:
      bools.append(False)

# Read space delimited integers from stdin and 
# pass a list of them to AreNumbersEven()
numbers = input()
integer_list = [int(i) for i in numbers.split(' ')]
even_odd_boolean_list = AreNumbersEven(integer_list)
print (even_odd_boolean_list)