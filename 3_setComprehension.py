fruits = {"apple", "apple", "cherry", "kiwi", "mango"}

newSet = set()

# Without comprehension
# for x in fruits:
#   if "a" in x:
#     newSet.add(x)

# Set comprehension in Python is a concise, single-line way to create a new set by iterating over an existing iterable (like a list, range, or string)
# and optionally applying transformations or filters
newSet = {x for x in fruits if 'e' not in x}

print(newSet)