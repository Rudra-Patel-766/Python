import random

i=0
while True:
    i+=1
    user_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissor: "))
    print(f"You choose {user_choice}")

    computer_choice = random.randint(0,2)
    print(f"Computer choose {computer_choice}")


    if user_choice >= 3 or user_choice < 0:
        print("You type an invalid number")
    elif user_choice==0 and computer_choice==2:
        print("You Win")
        break
    elif user_choice==2 and computer_choice==0:
        print("You Loose")
    elif user_choice==computer_choice:
        print("Draw")
    elif computer_choice > user_choice:
        print("You Loose")
    else:
        print("You Win")
        break
