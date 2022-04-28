from cressources import *
from cfunctions import *

def Continue():
    choice = input("\nWhat do you want to do?"
                   "\n1. Continue"
                   "\n2. Stop"
                   "\n3. Wallet"
                   "\n> ").lower()
    if choice.startswith("c") or choice == "1":
        return True
    elif choice.startswith("w") or choice == "3":
        walletShow(globals(pl))
        Continue()
    else:
        return False

def walletShow(user):

    print(f"\nAddress : {user.address}"
          f"\nSDC : {user.SDC}"
          f"\nUSD : {user.USD}")

def OnOff(var):
    if var == True:
        return "ON"
    else:
        return "OFF"