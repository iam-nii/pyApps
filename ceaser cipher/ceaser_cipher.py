alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(_text, _shift, _direction):
    cipher_text = ""  # Empty string to store the encrypted text
    _shift %= 26
    for letter in _text:

        if _direction == "encode":
            if letter not in alphabets:
                cipher_text += letter
            else:
                position = alphabets.index(letter)  # We get the position of the alphabet in the list
                new_position = position + _shift  # We find the new position by adding the shift to the position
                new_letter = alphabets[new_position]  # We get the alphabet at the new position
                cipher_text += new_letter  # We add the new alphabet to the cipher string
        elif _direction == "decode":
            if letter in alphabets:
                position = alphabets.index(letter)  # We get the position of the alphabet in the list
                new_position = position - _shift
                new_letter = alphabets[new_position]  # We get the alphabet at the new position
                cipher_text += new_letter  # We add the new alphabet to the cipher string
            else:
                cipher_text += letter

    print(f"The {_direction}ed text is {cipher_text}")


from art import logo
print(logo)

run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(text, shift, direction)
    restart = input("Do you want to restart the program? (yes/no): ")
    if restart == "yes":
        run = True
    elif restart == "no":
        print("Goodbye")
        run = False

