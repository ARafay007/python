animals = [
    {"name": "Python", "age": "23"},
    {"name": "Lion", "age": "12"},
    {"name": "Elephant", "age": "14"},
    {"name": "Zebra", "age": "18"},
]

animal = {}

# Dictionary comprehension is a concise and "Pythonic" way to create new dictionaries in a single line of code. It follows a syntax similar 
# to list comprehensions but uses curly braces {} and a key: value pair format. 
animal = {dict['name']: dict['age'] for dict in animals if dict['name'] == 'Python'}

print(animal)