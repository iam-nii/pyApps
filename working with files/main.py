# Reading from files
# file = open("text.txt")
# content = file.read()
# print(content)
# file.close()

# The 'with' keyword manages the opening and closing of files for us. Using 'with'
# We don't have to explicitly close open files
with open("text.txt") as my_file:
    content = my_file.read()
    print(content)

# Writing to files (Modes: read only('r'), append('a'), write('w'))
with open("text.txt", mode="a") as file:
    file.write("\n...Who am I kidding? I don't have free time lol")
