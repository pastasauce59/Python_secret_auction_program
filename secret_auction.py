from art import logo
print("Welcome to the secret auction. Please prepare to place your bids.")
print(logo)

more_bids = True
bidders = {}

while more_bids:
    name = input("What is your name? \n")
    bid = int(input("And what is your bid? \n$"))
    bidders[name] = bid

    contine_ = input("Are there any other bidders? Type \"Yes\" or \"No\" \n")
    if contine_.lower() != "yes":
        more_bids = False
        
        bidder_name = ''
        highest_bid = 0
        for bidder in bidders:
            if bidders[bidder] > highest_bid:
                bidder_name = bidder
                highest_bid = bidders[bidder]

        print(f"The winner is {bidder_name} with a bid of ${highest_bid}!")

    else:
        #works for VS Code to clear command line. #ymmv
        import os
        os.system('clear')