import random
item_list=['rock', 'paper', 'scissor']
user_choice=input("enter your choice (rock, paper, scissor): ")
comp_choice=random.choice(item_list)

print(f"user choice ={user_choice},computer_choice={comp_choice}")

if user_choice == comp_choice:
    print("It's a tie!")
elif user_choice == 'rock':
    if comp_choice == 'paper':
        print("Computer wins! Paper covers rock.")
    else:
        print("You win! Rock crushes scissor.")
elif user_choice == 'paper':
    if comp_choice == 'scissor':
        print("Computer wins! Scissor cuts paper.")
    else:
        print("You win! Paper covers rock.")
elif user_choice == 'scissor':
    if comp_choice == 'rock':
        print("Computer wins! Rock crushes scissor.")
    else:
        print("You win! Scissor cuts paper.")