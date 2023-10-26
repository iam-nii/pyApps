from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.left(120)
# timmy.color("yellow")
# timmy.forward(100)
# timmy.left(120)
# timmy.color("green")
# timmy.forward(100)
# timmy.color("coral")
#
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

# Constructing an object of class "PrettyTable"
table = PrettyTable()

# Adding data to the table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align['Pokemon Name'] = "r"
print(table)