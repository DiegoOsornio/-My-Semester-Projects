#Diego Osornio
#1/28/2025
import random
import time
import numpy as np
#Init
Symbol = ["♠", "♡", "7"]

money = 100
funds = 100
#Fun
def spinslot(bet):
    global funds
    global money

    weights = [0.7, 0.1, 0.2]

    funds = funds - bet

    spin1 = random.choice(Symbol)
    spin2 = random.choice(Symbol)
    spin3 = np.random.choice(Symbol, p=weights)

    # Adjust winnings based on the bet amount
    if spin1 == spin2 == spin3 == "7" and funds > 0:
        print("You got a Jackpot!")
        funds = funds + 10 * bet
        print(f"You won +{10 * bet} Credits!")

    if spin1 == spin2 == spin3 == "♠" and funds > 0:
        print("You Won!")
        funds = funds + 3 * bet
        print(f"+{3 * bet} Credits!")

    if spin1 == spin2 == spin3 == "♡" and funds > 0:
        print("You Won!")
        funds = funds + 3 * bet
        print(f"+{3 * bet} Credits!")

    if spin1 < spin2 < spin3 < "♡" and funds > 0:
        print("You lost -2 credits")
        funds = funds - 2 * bet

    if funds == 0:
        print("Insufficient Credits")

    print(spin1, spin2, spin3)




def slotmachine():
    global funds
    global money

    print("Welcome to the Slot Machine!")
    while True:
        bet = int(input("Enter your bet amount: "))
        if bet > funds:
            print("You don't have enough credits to place that bet.")
            continue

        spinslot(bet)
        time.sleep(1)

        review = input("Would you like to review your credits? (yes/no): ")
        if review.lower() == "yes":
            print(f"Your current credits:{funds}")

        spin_again = input("Do you want to spin again? (yes/no): ")
        if spin_again.lower() != "yes" :
            break





#Main


slotmachine()
