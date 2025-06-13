# Type Casting
# Implicit Type Casting
a = 10    # Integer
b = 3.5   # Float
c = a + b  # Implicitly converts 'a' to float
print("Implicit Type Casting: a + b =", c, "Type:", type(c))
# Explicit Type Casting
a = 10    # Integer
b = 3.5   # Float
c = int(b)  # Explicitly converts 'b' to integer
print("Explicit Type Casting: int(b) =", c, "Type:", type(c))
# Converting between types
a = 10    # Integer
b = "20"   # String
c = float(b)  # Converting string to float
print("Converting string to float: float(b) =", c, "Type:", type(c))
