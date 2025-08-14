dic = {
    "name": "John",
    "age": 30,
}
print(dic["name"])  # Accessing value by key , if key does not exist it raises KeyError
print(dic.get("age"))  # Using get method to access value by key , if key not exist returns None

print(dic.keys())  # Returns a view object that displays a list of all the keys in the dictionary
print(dic.values())  # Returns a view object that displays a list of all the values in the dictionary

print(dic.items())  # Returns a view object that displays a list of a dictionary's key-value tuple pairs

for key in dic.keys():
    print(key + " : " + str(dic[key]))  # Iterating over keys and printing key-value pairs


## Methods
city1 = {"delhi": 100, "mumbai": 200, "chennai": 300}
city2 = {"hydrabad": 150, "nanital": 250, "goa": 350}

city1.update(city2)  # Merging city2 into city1
print(city1)

city2.clear()  # Removing all items from city2
print(city2)  # city2 is now empty

city1.pop("delhi")  # Removing item with key 'delhi' from city1

city1.popitem()  # Removing the last inserted item from city1

del city2  # Deleting the entire city2 dictionary

del city1["mumbai"]  # Deleting the key 'mumbai' from city1

