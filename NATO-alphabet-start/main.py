student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
code_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in code_data_frame.iterrows():
#     print(row.letter)
#     print(row.code)

code_dictionary = {row.letter: row.code for(index, row) in code_data_frame.iterrows()}
#print(code_dictionary)
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Teachers approach
word = input("Enter a word: ").upper()
output = [code_dictionary[letter] for letter in word]
print(output)

#My approach lol
# user_input = list(input("Enter a word: ").upper())
# phonetic_list = [value for letter in user_input for (key, value) in code_dictionary.items() if letter == key]
# print(phonetic_list)
# for letter in user_input:
#     for (key, value) in code_dictionary.items():
#         if letter == key:
#             print(value)
