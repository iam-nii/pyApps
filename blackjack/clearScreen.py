from os import system, name


# define the clear function
def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')
