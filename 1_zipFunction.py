persons = ['James', 'Chandio', 'Peter', 'Lashari']
ages = [46,22,53,67,43]
cities = ['Jamshoro', 'New York', 'Tando Adam', 'Tokyo']

# The zip() function in Python is a built-in tool that aggregates elements from two or more iterables (like lists, tuples, or strings) into a single iterator of tuples. It is primarily used for parallel iteration and data reorganization.
for (name, age, place) in zip(persons, ages, cities):
    print(name, age, place)