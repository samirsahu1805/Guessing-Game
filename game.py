import random
import winsound

secret_number = random.randint(1, 50)
attempts = 0
max_attempts = 7

print("I have selected a number between 1 and 50.")
print("You have", max_attempts, "attempts.")

while attempts < max_attempts:
    user_input = input("Enter your guess: ")

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(user_input)

    if guess < 1 or guess > 50:
        print("Number must be between 1 and 50.")
        continue

    attempts += 1

    if guess > secret_number:
        print("Too High!")
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("\nYOU WON!")
        print("You guessed the number in", attempts, "attempts.")

        winsound.PlaySound("win.wav", winsound.win)
        break
else:
    print("\nYOU LOST!")
    print("The correct number was:", secret_number)

    winsound.PlaySound("lose.wav", winsound.lose)
