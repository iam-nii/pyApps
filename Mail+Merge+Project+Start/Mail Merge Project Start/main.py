with open("Input/Names/invited_names.txt", mode="r") as file:
    names = (file.read()).splitlines() # Removes the newline character at the end of every line


with open("Input/letters/starting_letter.txt", mode="r") as file:
    starting_letter = file.read()

for name in names:
    new_letter = starting_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(new_letter)