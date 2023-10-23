from operators import add, subtract, multiply, divide
from calc_art import logo
import math

# Storing the functions in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    # First number
    num1 = float(input("First number: "))
    continue_calc = True

    while continue_calc:
        # Operator
        for _operator in operations:
            print(_operator)
        operator = input("Operator: ")  # Selecting an operator

        # Second number
        num2 = float(input("Next number: "))
        # Here, we create a variable called function which is equal to the "value" of the
        # key "operator" depending on what the user selects. From here, we can use the
        # "Function" function as if it was any of the functions
        function = operations[operator]

        # We then create a variable to store the returned value from the function
        # This method is more efficient in the sense that instead of 5 if/else statements
        # to check which operator was selected, we just check the dictionary for the
        # Operator which is the key and take its implementation.
        result = function(num1, num2)

        print(f"{num1} {operator} {num2} = {result}")

        invalid = True
        while invalid:
            next = input(f"Type 'y' to continue calculating with {result}, 'new' to start a new calculation or"
                         f" type 'exit' to exit: ")

            if next == "y":
                continue_calc = True
                num1 = result
                invalid = False
            elif next == "exit":
                continue_calc = False
                invalid = False
            elif next == "new":
                calculator()
            else:
                print("Invalid input")
                invalid = True


calculator()
