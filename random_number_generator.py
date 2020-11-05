import random

def login():
    username = input("Please, enter your username : ")
    password = input("Please enter your password : ")

    if username == "darshan" and password == "Hindupurhbc123":
      print ("correct you have sucessfully login to the application!!")
      return True
    else:
      print("ypu have entered the wrong details, authentication failed    $$$$$$S ")
      return False


def start_game():
  if login():
    number = random.randint(1,10)
    chances = 0

    while chances < 10:
      print("the random number has been generated!!")
      gues = int(input("guess the number: "))
      chances = chances + 1

      if guess == number:
        print("congratulations you have won the game !!!!!!!")
        break

      elif guess < number:
       print("you are nearer to the number")
      elif guess > number:
       print("you are far from the number")

  if chances > 10:
    print("you have run out of your chances , GAME OVER !!!")

