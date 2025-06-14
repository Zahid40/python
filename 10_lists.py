marks = [98, 45, 89, 76, 88, 90, 100, 67, 45, 78]

print("Marks of the students are:", marks, "and type of marks is ", type(marks))
print("Length of marks is:", len(marks))
print("First element of marks is:", marks[0])

groceryList = ["apple", "banana", "cherry", "date"]
if "banana" in groceryList:
    print("Yes, 'banana' is in the list")

print(groceryList[1:-1])  # Slicing the list to get elements from index 1 to second last

# Jump indexing
print(groceryList[0:4:2])  # Getting every second element from the list

# List Comprehension
squaredMarks = [x**2 for x in range(1, 11)]
print("Squared marks are:", squaredMarks)

# List Comprehension with condition
evenSquaredMarks = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even squared marks are:", evenSquaredMarks)
