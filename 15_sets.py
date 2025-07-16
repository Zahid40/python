s = {2, 4, 2, 6}
print(s)  # Output: {2, 4, 6}

# Repeated values are ignored
# Sets are unordered collections of unique elements
# Sets are mutable, but elements must be immutable

print(type({}))  # Output: <class 'dict'>
print(type(set()))  # Output: <class 'set'> this is actually a empty set

## Methods of set
a = {1, 2, 3, 5}
b = {2, 4, 6, 7}
print(a.union(b))  # Output: {1, 2, 3, 4, 5, 6, 7}
print(a.intersection(b))  # Output: {2}
print(a.difference(b))  # Output: {1, 3, 5}

a.update(b)  # Adds elements of b to a
print(a)  # Output: {1, 2, 3, 4, 5, 6, 7}

city1 = {'Delhi', 'Mumbai', 'Bangalore'}
city2 = {'Mumbai', 'Chennai', 'Kolkata'}
city3 = city1.intersection_update(city2)  # Updates city1 with common elements
print(city3)  # Output: {'Mumbai'}
city4 = city1.symmetric_difference(city2)  # Elements in either city1 or city2 but not both
print(city4)  # Output: {'Delhi', 'Bangalore', 'Chennai', 'Kolkata'}

print(a.isdisjoint(b))  # Output: False (they have common elements)
print(a.issubset(b))  # Output: False (a is not a subset of b)
print(a.issuperset(b))  # Output: False (a does not contain all elements of b) 

# Adding elements
x = {a,b,c}
y = {d,e,f}
x.remove(a)  # Removes element a from x
x.discard(b)  # Removes element b from x, does not raise error if b is not present

item = x.pop()  # Removes and returns an arbitrary element from x
print(item)  # Output: an arbitrary element from x


## Removing and Deleting
# Clear
x.clear()  # Removes all elements from x, x becomes an empty set
# Delete
del x  # Deletes the set x