print("=== Iterables and Iterators ===")
my_list = [1, 2, 3]
it = iter(my_list)

print(next(it))  
print(next(it))  
print(next(it))  



print("\n=== Generator Example ===")
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)  


print("\n=== Comprehensions ===")

squares = [x**2 for x in range(5)]
print("List comprehension:", squares)

squares_dict = {x: x**2 for x in range(5)}
print("Dict comprehension:", squares_dict)


unique_lengths = {len(word) for word in ['hello', 'hi', 'world']}
print("Set comprehension:", unique_lengths)



print("\n=== Custom Iterator (Class-based) ===")
class CountDown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        val = self.n
        self.n -= 1
        return val

for num in CountDown(5):
    print(num)  




print("\n=== Custom Generator (yield) ===")
def countdown_gen(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown_gen(5):
    print(num)  


print("\n=== Infinite Prime Generator ===")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def infinite_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

prime_gen = infinite_primes()
for _ in range(10):
    print(next(prime_gen))
