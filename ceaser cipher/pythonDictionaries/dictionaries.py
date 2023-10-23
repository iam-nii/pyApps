programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A price of code that you can easily call over and over again.",
}

# Retrieving items from a dictionary.
print(programming_dictionary["Bug"])

# Adding items to a dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Creating an empty dictionary.
empty_dictionary = {}

# Editing an item in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Looping through a dictionary.
for key in programming_dictionary:
    print(key) # This prints the keys in the dictionary not because of the variable name assigned
    print(programming_dictionary[key])

# Wiping a existing dictionary.
programming_dictionary = {}
print(programming_dictionary)

##############################################################
# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Ghana": "Accra"
}

# Nesting a list in a dictionary.
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Hamburg", "Berlin", "Stuttgart"]
}

# Nesting a dictionary in a dictionary.
travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 0},
    "Germany": {"cities_visited": ["Hamburg", "Berlin", "Stuttgart"], "total_visits": 4},
    "Russia": {"cities_visited": ["Moscow", "St Petersburg"], "total_visits": 2}
}

# Nesting a dictionary in a list
travel_log3 = [
    {   # @index 0
        "country_visited": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 0
    },
    {   # @index 1
        "country_visited": "Germany",
        "cities_visited": ["Hamburg", "Berlin", "Stuttgart"],
        "total_visits": 4
    },
    {   # @index 2
        "country_visited": "Russia",
        "cities_visited": ["Moscow", "St Petersburg"],
        "total_visits": 2
    }
]
