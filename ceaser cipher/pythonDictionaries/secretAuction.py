from clearScreen import clear
print("Welcome to the secret auction.")

bidders_dictionary = {}
notDone = True
while notDone:
    bidder = input("What is your name?: ")
    bid = input("What's your bid? $")
    bidders_dictionary[bidder] = bid
    otherBidders = input("Are there other bidders? Type 'yes' or 'no'.\n")
    if otherBidders == "yes":
        notDone = True
        clear()
    elif otherBidders == "no":
        notDone = False
        clear()

# Getting the highest bidder
highest_bid = 0
highest_bidder = ""
for bidder in bidders_dictionary:
    if int(bidders_dictionary[bidder]) > highest_bid:
        highest_bid = int(bidders_dictionary[bidder])
        highest_bidder = bidder

# Displaying the winner
print(f"The winner is {highest_bidder} with a bid of {highest_bid}")