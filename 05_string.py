x = "Hello"
y = 'World'
z= """This is a
multi line string

Convenient for copy pasting
any string directly 
all backslash and tabs are handled 
"""

# print(x, y, z)

# Length of a string
print(len(x))  # Output: 5

# Slicing
names= "John, Jane, Doe"

print(names[0:4])
print(names[:4]) # default o before :


name="zahid"

print(name[:-2])
print(name[-2:len(name)-1])

# String methods
print(name.upper())  # Output: ZAHID
print(name.lower())  # Output: zahid
print(name.capitalize())  # Output: Zahid
print(name.title())  # Output: Zahid
print(name.swapcase())  # Output: ZAHID
print(name.replace("zahid", "John"))  # Output: John

print("john walker!!!!".rstrip("!"))  # Output: john walker
print("john walker!!!!".lstrip("!"))  # Output: john walker!!!!
print("john walker!!!!".strip("!"))  # Output: john walker

print("Welcome".center(20, "*"))  # Output: *****Welcome*****

print(name.startswith("z"))  # Output: True
print(name.endswith("d"))  # Output: True
print("Hello".count("l"))  # Output: 2
print("Hello".find("l"))  # Output: 2 (first occurrence) , if not found it returns -1

print("Hello".index("l"))  # Output: 2 (first occurrence) , if not found it raises ValueError

print("Hello123".isalnum())  # Output: True (contains letters and numbers)

print("Hello".isalpha())  # Output: True (contains only letters)

print("123".isdigit())  # Output: True (contains only digits)

print("hello".islower())  # Output: True
print("HELLO".isupper())  # Output: True


print("Hello\n".isprintable())  # Output: False (contains non printable characters \n)

print("   ".isspace())  # Output: True (contains only whitespace characters)

print("Hello World".istitle())  # Output: True (each word starts with an uppercase letter)
