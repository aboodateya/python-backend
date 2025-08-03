def generate_fibonacci (n):
    fib_series=[]
    c,d=0,1
    for _ in range(n):
      fib_series.append(c)
      c,d =d,c+d
    return fib_series

num = int(input("eneter how manynumbers you want:"))
print("fibonacci series:",generate_fibonacci(num))