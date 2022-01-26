# lambda arguments: expression
# example:
add10 = lambda x: x+10
print(add10(5)) # this will print 15

# using lambda to sort a list
# example:
points2D = [(1,2), (3,4), (5,6), (7,8)]
points2D.sort(key=lambda x: x[0]) # this will sort the list by the first value in the tuple
points2D.sort(key=lambda x: x[1]) # this will sort the list by the second value in the tuple
print(points2D) # this will print [(1, 2), (3, 4), (5, 6), (7, 8)]

# whats the time complexity of the above code?
# answer: O(n)

# here is another example:
points2D = [(1,2), (3,4), (5,6), (7,8)]
sorted_points2D = sorted(points2D, key=lambda x: x[0]+x[1]) # this will sort by the sum of first and second value in the tuple

# map(func,seq)
# map will apply a function to each item in a sequence. example:
a=[1,2,3]
b = list(map(lambda x: x+10, a)) # this will print [11, 12, 13]
# we can also use list comprehension:
c = [x+10 for x in a] # this will print [11, 12, 13]

# filter(func,seq)
# filter will apply a function to each item in a sequence. example:
a=[1,2,3]
b = list(filter(lambda x: x>2, a)) # this will print [3]
# we can also use list comprehension:
c = [x for x in a if x>2] # this will print [3]
# example: only return the even numbers
a=[1,2,3,4,5,6,7,8,9,10]
b= [x for x in a if x%2 ==0 ] # this will print [2, 4, 6, 8, 10]

# reduce(func,seq)
# reduce will apply a function to each item in a sequence and return one value. example:
from functools import reduce
a=[1,2,3,4]
sum_of_items = reduce(lambda x,y: x+y, a) # this will print 10
product_of_items = reduce(lambda x,y: x*y, a) # this will print 24