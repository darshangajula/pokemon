import random
from time import sleep

choices = ["charmender", "bulbosor", "squirtle"]

computer = random.choice(choices)

player = False
name = input("\n hello, please enter your name :")
while player ==  False:

    print ( f"\nhello,{name} welcome to pokemon battles game !!!!")
    player = input("which one do you want to choose? \n'charmender':'charmender'\n'squirtle':'squirtle'\n'bulbosor':'bulbosor'\n 'end the game':'stop'")
    if player == "computer":
        print("tie")
    elif player == "charmender":
        if computer == "squirtle":

            print ("\n please wait we are loading your results....")
            sleep(2)
            print("you loose")
        else:
            print("\n please wait we are loading your results....")
            sleep(2)
            print("you win")
    elif player == "bulbosor":
        if computer == "charmender":

            print("\n please wait we are loading your results....")
            sleep(2)
            print("you loose")
        else:
            print("\n please wait we are loading your results....")
            sleep(2)
            print("you win")
    elif player == "squirtle":
        if computer == "bulbosor":

            print("\n please wait we are loading your results....")
            sleep(2)
            print("you loose")
        else:
            print("\n please wait we are loading your results....")
            sleep(2)
            print("you win")

    elif player == "stop":
        print("thanks for playing")
        break
    else:
        print("thats not a valid ")
    player= False
