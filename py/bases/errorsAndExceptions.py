# to raise an Error:
x=3
if x<5:
    raise ValueError("x is less than 5")

# for assertion error:
assert x<5, "x is greater than 5"

# try/except/else/finally
# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass

try:
    a = 5/0
except Exception as e:
    print(e)
except TypeError as e:
    print(e)

## defining our own exceptions
class MyError(Exception):
    def __init__(self, message, value):
        self.value = value
        self.message = message
    def __str__(self):
        return repr(self.value)

def test_value(x):
    if x<0:
        raise MyError('x is less than 0', x)
    else:
        return x

try:
    test_value(-5)
except MyError as e:
    print(e.message, e.value)

