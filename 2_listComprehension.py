fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newList = []

# Without comprehension
for x in fruits:
  if "a" in x:
    newList.append(x)

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
newList = [x for x in fruits if 'e' in x]

print(newList)