## sudo random methods. These can be reproduceable by using the same seed.
# since these are reproducible, they are not suitable for cryptographic purposes.
import random
a = random.random() # random float 0.0 <= a < 1.0
b = random.randint(1,10) # random integer 1 <= b <= 10
c = random.randrange(1,10) # random integer 1 <= c < 10
d = random.normalvariate(0,1) # random float check the internet for diagram
e = random.choice(['a','b','c','d']) # random element from a sequence
f = random.sample(range(100), 10) # random sample from a sequence of size 10. elements are unique
myList = ["a","b","c","d"]
random.shuffle(myList) # random shuffle a sequence in place. Which means print(random.shuffle(myList)) will not work. And print(myList) will work.
print(myList)

# to reproduce the same random number we use a seed
random.seed(1)
a = random.random() 
b = random.randint(1,10) 
random.seed(1)
c= random.random()
d = random.randint(1,10)
print(a,b,c,d) # 0.0 1 1.0 1  # this is the same as the first random number


# fro more secure random we can use secrets module. It takes more time to generate a random number using this algorithm.
import secrets
a = secrets.token_hex(16) # 16 random hexadecimal characters
b = secrets.randbelow(100) # random integer 0 <= b < 100
c = secrets.randbits(8) # random integer 0 <= c < 2**8
d = secrets.choice(['a','b','c','d']) # random element from a sequence

# the another way is using numpy
import numpy as np
a = np.random.rand(3) # random float array
print(a) # [0.82409824 0.82409824 0.82409824]
b = np.random.randint(1,10,3) # random integer array. 10 is excluded. 1 <= b < 10
print(b) # [7 7 7]
c = np.random.randint(1,10,(3,3))
print(c)    # [ [7 7 7]
            #   [7 7 7]
            #   [7 7 7]]