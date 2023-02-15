from art import logo
print("Welcome to the secret auction. Please prepare to place your bids.")
print(logo)

more_bids = True
bidders = {}

def find_highest_bidder(bidding_dict):
    bidder_name = ''
    highest_bid = 0
    for bidder in bidding_dict:
        if bidding_dict[bidder] > highest_bid:
            bidder_name = bidder
            highest_bid = bidding_dict[bidder]
    print(f"The winner is {bidder_name} with a bid of ${highest_bid}!")

while more_bids:
    name = input("What is your name? \n")
    bid = int(input("And what is your bid? \n$"))
    bidders[name] = bid

    contine_ = input("Are there any other bidders? Type \"Yes\" or \"No\" \n")
    if contine_.lower() != "yes":
        more_bids = False
        find_highest_bidder(bidders)
    else:
        #works for VS Code to clear command line. #ymmv
        import os
        os.system('clear')