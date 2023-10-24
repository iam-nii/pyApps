from data import resources, menu
import sys

def getReport(_report):
    """Gets a report of the quantity of available resources"""
    water = _report['water']
    coffee = _report['coffee']
    milk = _report['milk']
    global profit
    return f"water : {water}ml\ncoffee: {coffee}g\nmilk: {milk}ml\nmoney: ${profit}"

def makeCoffee(_choice):
    """updates the resource dictionary depending on the order made"""
    _menu = menu[_choice]
    _milk = 0
    total = 0

    # Check how many resources are needed
    _ingredients = _menu['ingredients']
    _water = _ingredients['water']
    if _choice != "espresso":
        _milk = _ingredients['milk']
    _coffee = _ingredients['coffee']
    _cost = menu[_choice]['cost']

    # Reduce resources
    resources['water'] -= _water
    resources['milk'] -= _milk
    resources['coffee'] -= _coffee
    total += _cost

    global profit
    profit = total


def processCoins(_choice):
    """Checks to see if the money is sufficient and returns the total amount inserted"""
    print("Please insert coins.")
    total = float(input("How many quarters?: ")) * 0.25# 0.25
    total += float(input("How many dimes?: ")) * 0.10 # 0.10
    total += float(input("How many nickles?: ")) * 0.05 # 0.05
    total += float(input("How many nickles?: ")) * 0.01 # 0.01
    # Get the cost
    cost = menu[_choice]['cost']
    # Check if the customer put in enough coins
    if total < cost:
        print("Sorry, that's not enough. Money refunded.")
    else:
        change = round((total - cost), 2)
        print(f"Here is ${change} in change.")
        makeCoffee(_choice)
        print(f"Here is your {_choice} ☕, Enjoy!")


def checkResources(_choice):
    """Checks the resources to see if there are sufficient resources for the order"""
    insufficient = True
    _menu = menu[_choice]
    _milk = 0
    # Check how many resources are needed
    _ingredients = _menu['ingredients']
    _water = _ingredients['water']
    if _choice != "espresso":
        _milk = _ingredients['milk']
    _coffee = _ingredients['coffee']
    # print("Resource check")
    # print(_menu)
    # print(_ingredients)
    # print(_water)
    # if _choice != "espresso":
    #     print(_milk)
    # print(_coffee)

    for item in _ingredients:
        if _ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
        else:
            insufficient = False
    return insufficient


def checkInput(_choice):
    """Checks the users input"""
    if choice == 'off':
        sys.exit()
    elif choice == 'report':
        print(getReport(resources))
    else:
        insufficient = checkResources(_choice)
        if not insufficient:
            processCoins(_choice)


# Start program
profit = 0
while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    while choice != "espresso" and choice != "latte" and choice != "cappuccino"\
            and choice != "report" and choice != "off":
        print("Invalid choice")
        choice = input("What would you like? (espresso/latte/cappuccino):")
    checkInput(choice)
