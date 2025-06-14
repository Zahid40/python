## For Loop

# x = int(input("Enter a number for Table : "))
# for i in range(0, 10):
#     print(x, " X ", i + 1, " = ", x * (i + 1))


# colors=["red", "green", "blue", "yellow", "orange"]
# for color in colors : 
#     print(color.title()) 

# for i in range(1, 9, 2):
#     print(i) # output: 1, 3, 5, 7

# While Loop
x = 1
while x <= 10:
    print(x)
    x += 1

# break and continue
for i in range(1, 11):
    if i == 5:
        continue  # Skip the rest of the loop when i is 5
    print(i)  # Output: 1, 2, 3, 4, 6, 7, 8, 9, 10
    if i == 8:
        break  # Exit the loop when i is 8
