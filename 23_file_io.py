import os
os.mkdir("test.txt")
f= open("test.txt" , "r")
text = f.read()
print(text)
f.close()