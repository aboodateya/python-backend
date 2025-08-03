num= int(input("enter number:"))

if num <= 1 :
    print(" not a prime number")
else:
    i=2
    while i<num:
        if num%i==0:
          print("not a prime number")   
          break
        i=i+1
    else:
        print("its a prime number")