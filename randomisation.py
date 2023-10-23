import random

random_integer = random.randint(1, 200)
print(random_integer)

random_float = random.random() # Prints a random number between 0 and 1
print(random_float * 5) # Returns a random float between 0 and 5
print(random_float * 10) # Returns a random float between 0 and 10

# Heads or tails
side = random.randint(0, 1)
if side == 0:
    print("Tails")
else:
    print("Heads")