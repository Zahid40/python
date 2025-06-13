# Operators
# Arithmetic Operators
x = 10
y = 3
print("x + y =", x + y)  # Addition
print("x - y =", x - y)  # Subtraction
print("x * y =", x * y)  # Multiplication
print("x / y =", x / y)  # Division
print("x // y =", x // y)  # Floor Division
print("x % y =", x % y)  # Modulus
print("x ** y =", x ** y)  # Exponentiation

# Comparison Operators
print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)    # Greater than
print("x < y:", x < y)    # Less than
print("x >= y:", x >= y)  # Greater than or equal to
print("x <= y:", x <= y)  # Less than or equal to

# Logical Operators
print("x > 5 and y < 5:", x > 5 and y < 5)  # Logical AND
print("x > 5 or y < 5:", x > 5 or y < 5)    # Logical OR
print("not (x > 5):", not (x > 5))            # Logical NOT

# Assignment Operators
x = 10
x += 5  # x = x + 5
print("After x += 5, x =", x)
x -= 3  # x = x - 3
print("After x -= 3, x =", x)
x *= 2  # x = x * 2
print("After x *= 2, x =", x)
x /= 4  # x = x / 4
print("After x /= 4, x =", x)
x //= 2  # x = x // 2
print("After x //= 2, x =", x)
x %= 3  # x = x % 3
print("After x %= 3, x =", x)
x **= 2  # x = x ** 2
print("After x **= 2, x =", x)

# Bitwise Operators
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print("a & b =", a & b)  # Bitwise AND
print("a | b =", a | b)  # Bitwise OR
print("a ^ b =", a ^ b)  # Bitwise XOR
print("~a =", ~a)        # Bitwise NOT
print("a << 1 =", a << 1)  # Bitwise left shift
print("a >> 1 =", a >> 1)  # Bitwise right shift

# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)  # True, same object
print("x is z:", x is z)  # False, different objects
print("x is not y:", x is not y)  # False, same object
print("x is not z:", x is not z)  # True, different objects

# Membership Operators
print("2 in x:", 2 in x)  # True, 2 is in the list x
print("4 not in x:", 4 not in x)  # True, 4 is not in the list x

