import random
def generate_random_number(low, high):
    return random.randint(low, high)

def check_guess(secret_number, guess):
    if guess < secret_number:
        return "Too low !!!"
    elif guess > secret_number:
        return "Too high !!!"
    else:
        return "\nCorrect !!!"

secret_number = generate_random_number(1, 20)
guess = 0
guesses = 0
while(secret_number != guess):
    guess = int(input("Enter your guess: "))
    print(check_guess(secret_number, guess))
    guesses += 1
print("Number of guesses: ", guesses)



