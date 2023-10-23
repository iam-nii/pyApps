def format_name(firstName, lastName):
    """Take the first and last name and 
    return the title case version""" # This is called a Docstring
    if firstName == "" or lastName == "":
        return "You didn't provide valid inputs"
    formatted_fName = firstName.title()
    formatted_lName = lastName.title()
    return f"{formatted_fName} {formatted_lName}"


fullname = format_name(input("What is your first name?: "), input("What is your surname?: "))
print(fullname)