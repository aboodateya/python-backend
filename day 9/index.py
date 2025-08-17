import time
from functools import wraps


def outer_function(message):
    def inner_function():
        print(f"Message: {message}")
    return inner_function

closure_func = outer_function("Hello from closure!")
closure_func()  



def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' finished.")
        return result
    return wrapper

@log_function_call
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")



def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time for '{func.__name__}': {end - start:.4f} seconds")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(2)
    print("Slow function finished.")

slow_function()

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print(f"Content written to {filename}")


def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(f"Content of {filename}:\n{content}")

write_to_file("example.txt", "Hello from the context manager!\nThis was written using the 'with' statement.")
read_from_file("example.txt")


class CustomFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print(f"Closed file: {self.filename}")


with CustomFileManager("custom.txt", "w") as f:
    f.write("This was written using a custom context manager.")

