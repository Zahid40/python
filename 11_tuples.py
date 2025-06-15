tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6,) # if one value is a tuple, it must have a comma
print(type(tuple1))  # Output: <class 'tuple'>
print(tuple1[0])  # Output: 1

## Slicing
print(tuple1[1:3])  # Output: (2, 3)
print(tuple1[-1])  # Output: 5
print(tuple1[1:])  # Output: (2, 3, 4, 5)
print(tuple1[:3])  # Output: (1, 2, 3)
# with jump
print(tuple1[::2])  # Output: (1, 3, 5)

### Methods in tuple
countries = ("India", "USA", "China", "Japan", "Germany")
# print(countries.count("India"))  # Output: 1
# print(countries.index("Japan"))  # Output: 3
# print(countries.index("Japan" , 3,5))  # Output: 3
print(len(countries))  # Output: 5