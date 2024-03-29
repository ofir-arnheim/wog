import time
import random
import utils


# We override print line-breaks in order to re-write lines in the debugger console
# We also use our utils function screen clear for other consoles
# Time module is used to delay the re-write
def generate_sequence(difficulty):
    list_length = range(0, difficulty)
    numbers_list = [random.randint(1, 101) for i in list_length]
    for number in numbers_list:
        utils.screen_cleaner()
        print(f"\r{number}", end="")
        time.sleep(0.7)

    print(f"\rTime's up! ", end="")
    return numbers_list


# Split is used to create a list from a comma-separated string
# To accept spaces, strip is used to trim white-space values for int conversion
def get_list_from_users(difficulty):
    user_list_input = input(f"Which {difficulty} numbers were you just shown? (separated by a comma): ")
    try:
        user_list = [int(list_item.strip()) for list_item in user_list_input.split(",")]
    except ValueError:
        print("Input must be a list of numbers.")
        return None
    if len(user_list) != difficulty:
        print(f"Length of list must be {difficulty}.")
        return None
    return user_list


def is_list_equal(generated_sequence, user_list):
    if generated_sequence == user_list:
        print("Well done! You've memorized the numbers correctly!")
        return True
    else:
        print("Sorry, numbers are incorrect.")
        return False


def play(difficulty):
    generated_sequence = generate_sequence(difficulty)
    user_list = get_list_from_users(difficulty)
    return is_list_equal(generated_sequence, user_list)
