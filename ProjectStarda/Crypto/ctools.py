import re

def walletShow(user):

    print(f"\nAddress : {user.address}"
          f"\nSDC : {user.SDC}"
          f"\nUSD : {user.USD}")

def OnOff(var):
    if var == True:
        return "ON"
    else:
        return "OFF"

