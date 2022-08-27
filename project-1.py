import random
from winsound import PlaySound
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
Player = False
cpu_score = 0
player_score = 0
while True:
  player = input("Rock, Paper or Scissors?").capitalize()
  if player == computer:
    print("Tie!")
    elif player == "Rock":
      if computer == "Paper":
        print ("Lol", computer, "covers", player")
        cpu_score+=1
        else:
          print("You Win", player "smashes", computer")

          elif player == "End":
            print ("Final Scores:")
            print (f"CPU:{cpu_score}")
            print (f"CPU:{player_score}")
            break
            