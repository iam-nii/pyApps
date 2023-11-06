print("Welcome to the tip calculator")
bill = float(input("What was the total bill?: $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?: "))
num_of_people = int(input("How many people to split the bill?: "))

tip = (1 + percentage_tip/100) * bill

each_person = tip / num_of_people
final_amount = "{:.2f}".format(each_person)

print(f"Each person should pay: {final_amount}")