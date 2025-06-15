marks = [98, 45, 89, 76, 88, 90, 100, 67, 45, 78]

# print("Marks of the students are:", marks, "and type of marks is ", type(marks))
# print("Length of marks is:", len(marks))
# print("First element of marks is:", marks[0])

# groceryList = ["apple", "banana", "cherry", "date"]
# if "banana" in groceryList:
#     print("Yes, 'banana' is in the list")

## Slicing the list to get elements from index 1 to second last
# print(groceryList[1:-1])  

### Jump indexing
## Getting every second element from the list
# print(groceryList[0:4:2])  

# List Comprehension
squaredMarks = [x**2 for x in range(1, 11)]
# print("Squared marks are:", squaredMarks)

# List Comprehension with condition
evenSquaredMarks = [x**2 for x in range(1, 11) if x % 2 == 0]
# print("Even squared marks are:", evenSquaredMarks)


### List Methods
l = [5,1,3,4,7]
## Adding an element at the end
# l.append(6)  
## Sorting the list
# l.sort()  
# Reversing the list
## print("Sorted list :", l)
# l.reverse() 
## Getting the index of the element 4
# l.index(4)  
## Inserting 10 at index 2
# l.insert(2, 10)  
## Counting occurrences of 4 in the list
# l.count(4) 

# m=l
# Changing the first element of m will also change l since m is a reference to l
# m[0]=0 
# print("List l after modifications:", l)

# instead use copy()
## Creating a copy of the list
# l_copy = l.copy()  
## Changing the first element of l_copy won't affect l
# l_copy[0] = 10  

m=[110,999,809,1000,1001]
# l.extend(m)  # Extending list l with elements of m
k=l+m
print("Extended list l with elements of m:", k)
