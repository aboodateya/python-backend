from functools import wraps
def count_call(func):
    @wraps(func)
    def wrapper(*args, **kwrags):
        wrapper.call_count +=1
        print(f"[call #{wrapper.call_count}] Calling '{func.__name__}'")
        return func(*args, **kwrags)
    wrapper.call_count =0
    return wrapper

@count_call
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Alice")
    greet("Bob")
    greet("Charlie")
    print("Total calls to greet:", greet.call_count)  # 3

