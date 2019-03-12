from random import randint 
print("enter your choice from\nrock(O), paper(__), scissors(>8)\npress r for rock\npress p for paper\npress s for scissors")
player = input("you press: ")

if player == "r":
 print("O", end=" ")

elif player == "p":
 print("__", end=" ")

elif player == "s":
 print(">8", end=" ")

else:
 print("Wrong Choice")

print("vs", end=" ")

#module implementation

chosen = randint(1,3)

if chosen == 1:
 computer = "r"
 print("O")

elif chosen == 2:
 computer = "p"
 print("__")

else:
 computer = "s"
 print(">8")

if player == computer:
 print("Draw!\nwell played")

elif player == "r" and computer == "p":
 print("computer wins!\nbetter luck next time")

elif player == "r" and computer == "s":
 print("you wins!\nwell played")

elif player == "p" and computer == "s":
 print("computer wins!\nbetter luck next time")

elif player == "p" and computer == "r":
 print("you wins!\nwell played")

elif player == "s" and computer == "p":
 print("you wins!\nwell played")

elif player == "s" and computer == "r":
 print("computer wins!\nbetter luck next time")

else:
 print("Something Went Wrong.. Sorry!")
