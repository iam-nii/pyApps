from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOn = True
# Constructing objects of the CoffeeMaker and MoneyMachine Classes
coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

while isOn:
    choice = input(f"What would you like? {menu.get_items()}: ")
    item = menu.find_drink(choice)
    if choice == "off":
        isOn = False
    elif choice == "report":
        coffeeMachine.report()
        moneyMachine.report()
    elif choice != "off" and choice != "report" and choice != "espresso" and choice != "latte" and \
            choice != "cappuccino":
        print("Invalid input")
    else:
        if coffeeMachine.is_resource_sufficient(item):
            cost = item.cost
            if moneyMachine.make_payment(cost):
                coffeeMachine.make_coffee(item)





