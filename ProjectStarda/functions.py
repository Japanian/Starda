import time
import random
from tools import *
from ressources import *
import os

# quiz

def quiz():
    print("\nOkay, let's go for the quiz!")
    print("First, let me explain, I will ask questions and you will awnser, your awnsers"
          "will be saved for data analysis purposes")

    print("\nWarning : Your information may be collected, they will be used to improve this chatbot")

    time.sleep(2)

    while True:
        print("\nQuestion 1:"
              "\nChoose a number between 1 and 10")
        q1 = int(input("> "))
        if q1 == 0 or q1 > 10:
            print("Hey, i said a number between 1 and 10")
            continue
        else:
            break

    quizDataSave(q1)


# Rock paper scissors

def rps():
    global winned
    awnser = random.choice(rpsAwnser)
    print(awnser)
    print("\nWarning : Your information may be collected, they will be used to improve this chatbot")
    time.sleep(2)

    botWin = 0
    userWin = 0
    actions = ["Rock", "Paper", "Scissors"]
    botChoices = ["Rock", "Paper", "Scissors"]

    if rpsDataActions() == "Rock":
        botChoices.append("Paper")
    elif rpsDataActions() == "Paper":
        botChoices.append("Scissors")
    elif rpsDataActions() == "Scissors":
        botChoices.append("Rock")

    while True:
        print("\nChoose your action :"
              "\nA - Rock"
              "\nB - Paper"
              "\nC - Scissors")
        action = input("> ").lower()
        if action.startswith("a"):
            userAction = actions[0]
        elif action.startswith("b"):
            userAction = actions[1]
        elif action.startswith("c"):
            userAction = actions[2]
        else:
            print("huh? Can you repeat?")
            continue

        botAction = random.choice(botChoices)

        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        print(f"\nI choose {botAction}!")

        if userAction == "Rock" and botAction == "Scissors" or userAction == "Paper" and botAction == "Rock" or userAction == "Scissors" and botAction == "Paper":
            print("\nYou won, GG! :)")
            winned = "user"
            userWin += 1
            print(f"You now have {userWin} win(s)")

        elif botAction == "Rock" and userAction == "Scissors" or botAction == "Paper" and userAction == "Rock" or botAction == "Scissors" and userAction == "Paper":
            print("\nYay! I won :)")
            winned = "bot"
            botWin += 1
            print(f"I now have {botWin} win(s)")

        elif botAction == userAction:
            winned = "null"
            print("Oops, no one won :'(")

        else:
            print("Something goes wrong")

        time.sleep(1.5)

        rpsDataSave(userAction, botAction, winned)

        print("\nDo you want to replay?")
        choice = input("> ").lower()
        if choice.startswith("y"):
            pass
        else:
            break

def uno():
    print("Okay let's play UNO")


# Utilities

def resetLobby():
    while True:
        print("\nWhat do you want to reset?"
              "\nA - Quiz"
              "\nB - Rock Paper Scissors")
        menu = input("> ").lower()
        if menu == "a":
            reset("quiz")
            print("Reset completed")
            time.sleep(1)
            os.system("clear")
            break
        elif menu == "b":
            reset("rps")
            print("Reset completed")
            time.sleep(1)
            os.system("clear")
            break
        else:
            print("a or b only")

def math():
    while True:
        print("\nChoose a number form"
              "\nA - Int (1)"
              "\nB - Float (1.0)")
        form = input("> ").lower()
        if form.startswith("a"):
            print("\nEnter the first term")
            first = int(input("> "))
            print("\nEnter the second term")
            second = int(input("> "))


            print("\nChoose a symbol :"
                  "\nA - +"
                  "\nB - -"
                  "\nC - /"
                  "\nD - *")
            menu = input("> ").lower()

            if menu.startswith("a"):
                result = first + second
                print(f"The result is {result}")
            elif menu.startswith("b"):
                result = first - second
                print(f"The result is {result}")
            elif menu.startswith("c"):
                result = first / second
                print(f"The result is {result}")
            elif menu.startswith("d"):
                result = first * second
                print(f"The result is {result}")

        elif form.startswith("b"):
            print("\nEnter the first term")
            first = float(input("> "))
            print("\nEnter the second term")
            second = float(input("> "))

            print("\nChoose a symbol :"
                  "\nA - +"
                  "\nB - -"
                  "\nC - /"
                  "\nD - *")
            menu = input("> ").lower()

            if menu.startswith("a"):
                result = first + second
                print(f"The result is {result}")
            elif menu.startswith("b"):
                result = first - second
                print(f"The result is {result}")
            elif menu.startswith("c"):
                result = first / second
                print(f"The result is {result}")
            elif menu.startswith("d"):
                result = first * second
                print(f"The result is {result}")

        print("\nDo you want to restart?")
        re = input("> ")
        if re.startswith("y"):
            continue
        else:
            break



