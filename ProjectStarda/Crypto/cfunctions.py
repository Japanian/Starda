from cressources import *
from ctools import *
from pprint import pprint
from random import choice, randint
import os

def beginning():
    global pl
    print("Hello and welcome to CryptoGame made by Japanian and powered by Starda!")
    print("In this game you will have to mine, trade and collect Crypto")

    print("\nSo because you begin, I will give you 10 StardaCoin (SDC) and 10 USD")
    name = input("Can you give me your username so I can sent you the SDC?"
                 "\n> ")

    pl = wallet(10, 10, f"{name}.wallet")

    bc.new_transaction(Starda, pl, 10, "SDC")
    bc.new_transaction(Starda, pl, 10, "USD")

    print(f"\nSent to {pl.address}")
    print("So now, goodluck and goodbye (if you want to exit you can at anytime do /starda)")
    os.system("clear")
    hub()

def hub():
    menu = input("\nWhat do you want to do?"
                 "\n1. Trade"
                 "\n2. Mine"
                 "\n> ").lower()

    if menu == "trade" or menu == "1":
        trade()

    elif menu == "mine" or menu == "2":
        mine()

    elif menu == "/starda":
        pass

    elif menu == "/settings":
        pass

def trade():
    pass

def mine():
    global finish
    gain = 0.5
    chain = 0
    while not finish:
        sender = choice(people)
        people.remove(sender)
        receiver = choice(people)
        people.append(sender)
        amount = randint(1, sender.SDC)

        bc.new_transaction(sender, receiver, amount, "SDC")

        word = choice(words)

        while not finish:
            type = input(f"\n{word}"
                         f"\n> ")

            if type == word:
                if chain >= 1:
                    gain += 0.5
                chain += 1
                print(f"Good job! {gain} SDC earned")
                pl.SDC += gain
                print(f"Chain +1, current chain: {chain}")
                break

            elif type == "exit":
                print("\nExited mining")
                finish = True
                break
            else:
                gain = 0.5
                chain = 0
                print("Oops, chain broken")
                break

        if finish == True:
            break

        if askReplay == True:
            if Continue() == False:
                break
    finish = False

def settings():
    category = input("\nSelect a category :"
          "\n1. Trade"
          "\n2. Mine"
          "\n> ").lower()

    if category.startswith("t") or category == "1":
        pass
    elif category.startswith("m") or category == "2":
        while True:
            print(f"\nHere are the current settings :"
                  f"\nA - Ask Replay : {OnOff(askReplay)}")
            setting = input("\nSelect the letter of the desired settings (or type exit)").lower()

            if setting == "a":
                askReplay = False



