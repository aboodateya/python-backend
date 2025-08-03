def factorial(n):
  if n==0 or n==1:
    return 1
  print(n)
  return n* factorial(n-1)

number=int(input("enter number"))
result = factorial(number)
print ("factorial of", number, "is",result)