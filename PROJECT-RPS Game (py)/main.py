print("welcome to Rock,Paper and Scissors Game")
input = int(input("Which one you wnat to choose : \n1)Rock\n2)Paper\n3)Scissors\n= "))

if(input == 1):
    u_choice = "rock"
elif(input == 2):
    u_choice = "paper"
elif(input == 3):
    u_choice = "scissors"
print(f"Your Choice :",u_choice)

import random
list = ["rock","paper","scissors"]
cp_choice = random.choice(list)
print(f"Oppenent's Choice :",cp_choice)

if(u_choice == cp_choice):
    print("It's a Draw")
else:
    if(u_choice == "rock" and cp_choice == "scissors"):
        print("You win")
    elif(u_choice == "scissors" and cp_choice == "paper"):
        print("You win")
    elif(u_choice == "paper" and cp_choice == "rock"):
        print("You win")
    else:
        print("You lose")
