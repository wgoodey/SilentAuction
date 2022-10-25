import art
import os

bids = []


def add_bid(bidder_name, bidder_amount):
    new_bid = {
        "name": bidder_name,
        "amount": bidder_amount
    }
    bids.append(new_bid)


def get_highest_bidder():
    highest_bid = 0
    bidder_name = ""

    for bid in bids:
        if bid["amount"] > highest_bid:
            highest_bid = bid["amount"]
            bidder_name = bid["name"]

    print(f"The highest bidder is {bidder_name}, with ${highest_bid}.")


def get_bid():
    name = input("Enter your name: ")
    bid = 0
    while bid == 0:
        try:
            bid = int(input("Enter your bid: "))
        except ValueError:
            print("Please enter an integer for the bid value.")
    add_bid(name, bid)


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


get_another = True

while get_another:
    print(art.logo)
    print("Welcome to the blind auction.")
    get_bid()
    more_bidders = input('Are there any more bidders? Type "yes" if there are.\n')
    if more_bidders != "yes":
        get_another = False
    clear_screen()

get_highest_bidder()
