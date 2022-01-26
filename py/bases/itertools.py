# product
from itertools import product
a=[1,2]
b=[3,4]
prod = product(a,b)
print(list(prod)) # this will print [(1, 3), (1, 4), (2, 3), (2, 4)]

# permutations
from itertools import permutations
a=[1,2,3]
perm = permutations(a)
print(list(perm)) # this will print [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# we can specify the number of items to permute. example:
perm = permutations(a,2)
print(list(perm)) # this will print [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations
# despite permutations, there will be no repetition. example:
from itertools import combinations
a=[1,2,3]
comb = combinations(a,2)
print(list(comb)) # this will print [(1, 2), (1, 3), (2, 3), (3, 2)]

# accumulate
# accumulate will take a list and return a list of the sums of the items up to current index in the list. example:
from itertools import accumulate
a=[1,2,3,4,5]
acc = accumulate(a)
print(list(acc)) # this will print [1, 3, 6, 10, 15]

# we can also specify a function to use for the accumulation. example:
from itertools import accumulate
a=[1,2,3,4,5]
acc = accumulate(a, lambda x, y: x + y) # this will add the items in the list
acc = accumulate(a, lambda x, y: x * y) # this will print [1, 2, 6, 24, 120]
acc = accumulate(a, lambda x, y: x + y, 0) # this will start the accumulation at 0
acc = accumulate(a, lambda x,y:x>y) # this will return a list of booleans

# or use operator
from itertools import accumulate
import operator
a=[1,2,3,4,5]
acc = accumulate(a, operator.add) # this will print [1, 3, 6, 10, 15]
acc = accumulate(a, operator.mul) # this will print [1, 2, 6, 24, 120]
acc = accumulate(a, operator.sub) # this will print [1, -1, -3, -5, -9]
acc = accumulate(a,func=operator.max) # this will print [1, 2, 3, 4, 5]
acc = accumulate(a,func=operator.min) # this will print [1, 1, 1, 1, 1]

# groupby
# groupby will group items in a list by a key. example:
from itertools import groupby
def smaller_than_3(x):
    return x < 3

a=[1,2,3,4,5,6,7,8,9,10]
group = groupby(a, key=smaller_than_3)
# group = groupby(a, key=lambda x: x < 3)
print(list(group)) # this will print [(False, [1, 2, 3]), (True, [4, 5, 6, 7, 8, 9, 10])]

# example of dict
persons = [
    {'name': 'John', 'age': 20},
    {'name': 'Bob', 'age': 30},
    {'name': 'Mary', 'age': 25},
    {'name': 'Jane', 'age': 31},
    {'name': 'Jack', 'age': 20}
]
grouped_persons = groupby(persons, key=lambda x: x['age'])
print(list(grouped_persons)) 
# this will print:
# [
#     (20, [{'name': 'John', 'age': 20}, {'name': 'Jack', 'age': 20}]),
#     (30, [{'name': 'Bob', 'age': 30}]), (25, [{'name': 'Mary', 'age': 25}]),
#     (31, [{'name': 'Jane', 'age': 31}])
# ]


# count
# count will count the number of items in a list. example:
from itertools import count
for i in count(3): #3 is the starting number
    print(i)
    if i > 10:
        break
# this will print:
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# cycle
# cycle will cycle through a list. example:
from itertools import cycle
a=[1,2,3]
for i in cycle(a):
    # print(i) # this will print infinitely
    break

# we can specify the number of times to cycle through the list. example:
for i in cycle(a,3):
    print(i) # this will print 1,2,3,1,2,3,1,2,3

# repeat
# repeat will repeat a list a specified number of times. example:
from itertools import repeat
a=[1,2,3]
for i in repeat(a,3):
    print(i) # this will print 1,2,3,1,2,3,1,2,3
    



