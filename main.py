'''
def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet("mummy")
'''


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in  {location}?")


greet_with(location="Canada", name="James") # Keyword arguments passed the values based on their assignments when called
greet_with("James", "Canada") # Positional arguments are arguments passed in the order they are presented