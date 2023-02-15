from art import logo
print("Welcome to the secret auction. Please prepare to place your bids.")
print(logo)

more_bids = True
bidders = {}

while more_bids:
    name = input("What is your name? \n")
    bid = input("And what is your bid? \n$")
    bidders[name] = bid

    # print(bidders)
    contine_ = input("Are there any other bidders? Type \"Yes\" or \"No\" \n")
    if contine_.lower() != "yes":
        more_bids = False
        print(bidders)
    else:
        #works for VS Code to clear command line. #ymmv
        import os
        os.system('clear')