import random
secret_number = random.randint(1,10)

guess_count = 0
guess_limit = 3

print("You have three guesses")
while guess_count < guess_limit:
    if guess_count == 0:
        guess = int(input("Guess a number between 1 and 10: "))
        guess_count += 1
        if guess == secret_number:
            print("You Won")
            break
    else:
        guess = int(input("Guess again: "))
        guess_count += 1
        if guess == secret_number:
            print("You Won")
            break
else:
    print(f"You Lost! The number was {secret_number}")

