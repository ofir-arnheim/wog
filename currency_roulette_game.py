import requests
import random


# We call the API directly from our code. API has a limit of 1000 requests per month.
# Failed API requests can come from a multitude of reasons, so a catchall except is used
def get_money_interval(difficulty, usd_amount):
    base_url = 'https://openexchangerates.org/api/latest.json'
    params = {
        'app_id': '6b88319f38db48939ad07d99aa9aa274',
        'symbols': 'ILS',
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        usd_to_ils_conversion_rate = int(data['rates'].get('ILS'))
    except:
        print("Unable to get API request.")
        return None
    calculated_difficulty = 10-difficulty
    ils_amount = usd_amount * usd_to_ils_conversion_rate
    guess_interval = range(ils_amount-calculated_difficulty, ils_amount+calculated_difficulty)
    return guess_interval


# We convert the guess parameter to int if we receive a float.
# This makes it less accurate, but fine since we're dealing with a mistake range of 0-10.
def get_guess_from_user(usd_amount):
    guess = input(f"What is the current value of ${usd_amount} USD in NIS? ")
    try:
        guess_as_float = float(guess)
        guess_as_int = int(guess_as_float)
        return guess_as_int
    except ValueError:
        print("Guess must be a number.")


def compare_results(guess, guess_interval):
    if guess in guess_interval:
        print("Congrats, your guess was close enough!")
        return True
    else:
        print("Sorry, your guess was not close enough.")
        return False


# We use this function to generate the USD number and call our functions.
# API request failure is also handled here.
# We also add a check on the difficulty param here.
def play(difficulty):
    if difficulty.isdigit and 1 <= int(difficulty) <= 10:
        difficulty = int(difficulty)
    else:
        print("Difficulty must be a number between 1 and 10.")
        return None
    usd_amount = random.randint(1, 100)
    guess_interval = get_money_interval(difficulty, usd_amount)
    if guess_interval is not None:
        guess = get_guess_from_user(usd_amount)
        return compare_results(guess, guess_interval)

