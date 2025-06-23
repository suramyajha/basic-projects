import random

print("Welcome to Rock, Paper, Scissor Game!")

random_number = random.randint(1, 3)
dictnum = {1: "rock", 2: "paper", 3: "scissor"}

user_choice = input("Enter your choice (rock, paper, scissor): ").lower()

if user_choice not in dictnum.values():
    print("Invalid choice! Please choose rock, paper, or scissor.")
    exit()

computer_choice = dictnum[random_number]
print("Computer chooses:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissor") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissor" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
