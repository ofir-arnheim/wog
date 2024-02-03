import random


# Using the random library, we generate a number between 0 and the difficulty int
# We verify the difficulty int in other functions
def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    return secret_number


# Using the difficulty int, we prompt the user to guess
def get_guess_from_user(difficulty):
    guess = input(f"Type a number between 0 and {difficulty}: ")
    if guess.isnumeric() and 0 <= int(guess) <= difficulty:
        return int(guess)
    else:
        print(f"Guess must be a number between 0 and {difficulty}.")


# We compare the results using the ints we got from the other functions
def compare_results(secret_number, guess):
    if secret_number == guess:
        print(f"You guessed correctly! Number is {secret_number}!")
        return True
    else:
        print(f"Incorrect guess. Number is {secret_number}.")
        return False


# We add a check on the difficulty param here.
def play(difficulty):
    if difficulty.isdigit and 1 <= int(difficulty) <= 100:
        difficulty = int(difficulty)
    else:
        print("Difficulty must be a number between 1 to 100.")
        return None
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, guess)
