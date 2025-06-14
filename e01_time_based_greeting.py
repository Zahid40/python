import time
print(time.asctime())

name= input("Enter your name: ")
if time.localtime().tm_hour < 12:
    print(f"Good morning, {name}!")
elif time.localtime().tm_hour < 18:
    print(f"Good afternoon, {name}!")
else:
    print(f"Good evening, {name}!")
    