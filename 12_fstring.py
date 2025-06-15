letter = "Hey my name is {} and I am from {}"
name = "John"
city = "New York"
print(letter.format(name, city)) # output: Hey my name is John and I am from New York

# Using f-string for formatting
print(f"Hey my name is {name} and I am from {city}") # output: Hey my name is John and I am from New York

print(f"Price of the item is {19.6789:.2f}")  # output: Price of the item is 19.68