import random

h = 100
l = 1
answer = random.randint(l, h)

is_running = True
guesses = 0

while is_running:
    num = input(f"Enter a number between {l} and {h}: ")

    if not num.isdigit():
        print("Enter a valid number.")
        continue

    num = int(num)
    guesses += 1

    if num > h or num < l:
        print(f"Please only enter a number between {l} and {h}.")
        continue

    

    if num == answer:
        print("Congratulations! You guessed the number.")
        is_running = False
        print (f"Amount of times you guessed is {guesses}")

    elif num < answer:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")



print("Game Over")
