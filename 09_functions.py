def geometric_mean(a, b):
    mean = (a * b) / (a + b)
    print("Geometric Mean of ", a, "and", b, "is", mean)

def isLesser(a,b):pass # This function is not implemented yet

geometric_mean(5, 4)

def line(z , x , c=0):
    print(f"y = {x}x + {z}z + {c}")

line(2, 3, 4)  # Output: y = 2 x + 4
line(2, 3)  # Output: y = 3 x


# Variable arguments
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of numbers:", add(1, 2, 3, 4, 5))  # Output: Sum of numbers: 15

# Keyword arguments
def student_info(name, age, **kwargs):
    print(f"Name: {name}\nAge: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info("Alice", 20, major="Computer Science", university="XYZ University")