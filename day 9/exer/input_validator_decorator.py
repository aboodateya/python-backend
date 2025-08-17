from functools import wraps
def validate_positive(func):
   
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Invalid argument: {arg}. Must be a positive number.")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def divide(a, b):
    return a / b
if __name__ == "__main__":
    print("10 / 2 =", divide(10, 2))  
