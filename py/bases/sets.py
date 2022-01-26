

### sets
# create a set
set1 = {1, 2, 3, 4, 5}
# or
set2 = set([1, 2, 3, 4, 5])
print(set1)
print(set2)

# we can use sets to find the unique items in a list
# example:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,3,4]
set7 = set(list1)
print(set7) # this will print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# add to a set
set1.add(6)
print(set1)

# remove from a set. this will throw an error if the item is not in the set
set1.remove(6)
print(set1)

# remove from a set by value. this will not throw an error if the value is not in the set
set1.discard(6)
print(set1)

# copy a set
set3 = set1.copy()
# or set3 = set(set1)
print(set3) # this will print {1, 2, 3, 4, 5}. if we change set1, set3 will not change.

# combine two sets
set3 = set1.union(set2)
print(set3)

# find the difference between two sets
set4 = set1.difference(set2)
print(set4)

# find the intersection between two sets
set5 = set1.intersection(set2)
print(set5)

# symmetric difference. this is the set of items that are in one set or the other, but not both
set6 = set1.symmetric_difference(set2)
print(set6)

# update a set
set1.update([11, 12, 13])
print(set1) # this will print {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

# check if a set is subset of another set
set1.issubset(set2)
print(set1.issubset(set2)) # this will print False

# check if a set is superset of another set
set1.issuperset(set2)
print(set1.issuperset(set2)) # this will print False.

# check if a set is disjoint with another set
set1.isdisjoint(set2)
print(set1.isdisjoint(set2)) # this will print True.

# frozenset. this is a set that cannot be changed.
set8 = frozenset([1, 2, 3, 4, 5])
print(set8)










