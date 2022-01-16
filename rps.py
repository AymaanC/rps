import random
import time
rr = "yes"
while rr == "yes":
    usr = input("Choose : Rock, Paper, Scissors - ")
    comp = ["rock", "paper", "scissors"]
    r = random.choice(comp)
    print("You chose : "+usr)
    print("----------------------")
    print("Computer chose : "+r)
    print("----------------------")
    if usr.lower() == "rock":
        if r == "paper":
            print("you lose")
    if usr.lower() == "rock":
        if r == "rock":
            print("its a tie")
    if usr.lower() == "rock":
        if r == "scissors":
            print("you win")
    if usr.lower() == "paper":
        if r == "paper":
            print("its a tie")
    if usr.lower() == "paper":
        if r == "rock":
            print("you win")
    if usr.lower() == "paper":
        if r == "scissors":
            print("you lose")
    if usr.lower() == "scissors":
        if r == "paper":
            print("you win")
    if usr.lower() == "scissors":
        if r == "rock":
            print("you lose")
    if usr.lower() == "scissors":
        if r == "scissors":
            print("its a tie")
    print("----------------------")
    ans = input("Do you want to play again? Y/N ")
    if ans.lower() == "y":
        rr = "yes"
    elif ans.lower() == "n":
        rr = "no"
    else:
        print("undefined answer, shutting down program")
        time.sleep(1)
        rr = "no"
