## Collections
# Counter
from collection import Counter
my_string = "Hello World"
print(Counter(my_string)) # this will print Counter({'l': 2, 'o': 2, 'r': 1, 'd': 1, 'H': 1, 'e': 1, 'W': 1, ' ': 1})
print(Counter(my_string).most_common(2)) # this will print [('l', 2), ('o', 2)]
print(Counter(my_string).most_common(1)) # this will print [('l', 2)]
print(Counter(my_string).keys()) # this will print dict_keys(['l', 'o', 'r', 'd', 'H', 'e', 'W', ' '])
print(Counter(my_string).values()) # this will print dict_values([2, 2, 1, 1, 1, 1, 1, 1])

# namedtuple
from collections import namedtuple
Point = namedtuple("Point",'x,y')
p = Point(1,2)
print(p.x) # this will print 1
print(p) # this will print Point(x=1, y=2)

# OrderedDict
# They are used to preserve the order of the items in a dictionary. But in Python 3.7, they are no longer needed and normal dictionaries are ordered by default.
from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d) # this will print OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# deque
# deque is a double-ended queue. It can be used to add or remove items from both ends of the list. It is also known as a "doubly-ended queue" or "deque".
# It is a more efficient version of a list. especially when you are dealing with large lists.
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)
# first item


print(d) # this will print deque([1, 2, 3])
d.popleft()
print(d) # this will print deque([2, 3])
d.pop()
print(d) # this will print deque([2])
d.extend([4,5,6])
print(d) # this will print deque([2, 4, 5, 6])
d.extendleft([7,8,9])
print(d) # this will print deque([7, 8, 9, 2, 4, 5, 6])
d.rotate(3) # this will move the items to the right 3 times
print(d) # this will print deque([4, 5, 6, 7, 8, 9, 2])
d.rotate(-3) # this will move the items to the left 3 times
print(d) # this will print deque([2, 4, 5, 6, 7, 8, 9])
d.reverse()
print(d) # this will print deque([9, 8, 7, 6, 5, 4, 2])

