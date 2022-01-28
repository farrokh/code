
## function decorators
# to preserve the original function name, we can use the @ symbol
import functools


def mydecorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): # *args and **kwargs are the arguments and keyword arguments of the function
        print("Before the function")
        result = func(*args, **kwargs)
        print("After the function")
        return result

@mydecorator
def myfunction(a, b):
    return a + b
    return wrapper

# example 2:
def repeat(num_times):
    def decoratorRepeat(func):
        @functools.wraps(func)
        def wrapperRepeat(*args, **kwargs):
            for i in range(3):
                result = func(*args, **kwargs)
                print(result)
        return wrapperRepeat
    return decoratorRepeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')