# Decorator Method is a Structural Design Pattern which allows you to dynamically attach new behaviors to objects without changing their implementation
# by placing these objects inside the wrapper objects that contains the behaviors.

# Function-Based Decorators
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

# Usage
add(5, 3)


# Class-Based Decorators
import time

class Timer:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
            return result
        return wrapper

@Timer()
def slow_function():
    time.sleep(2)
    print("Function finished!")

# Usage
slow_function()
