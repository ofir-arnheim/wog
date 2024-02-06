from games import currency_roulette_game, guess_game, memory_game
import score


# A welcome message for the user, validating the username.
# In the future, we can import the string library or use regular expressions to be more flexible.
def welcome():
    username = input("What is your username? ")
    if username.isalnum() is False:
        print("Invalid input. Username can contain only letters and numbers.")
    elif len(username) > 20:
        print("Invalid input. Username cannot be over 20 in length.")
    else:
        print("Hi " + username + " and welcome to the World of Games: The Epic Journey")
        return username


# A prompt where the user decides which game to play, using the listed numbers.
# We print the output of our games, which currently return only True or False
# If the user does not enter a number between 1 and 3, we present an error.
def start_play():
    game = input("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
    guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    : """)
    games_list = ["Memory Game", "Guess Game", "Currency Roulette"]
    games_dict = {
        1: memory_game.play,
        2: guess_game.play,
        3: currency_roulette_game.play,
    }
    while True:
        if game.isdigit() and 0 < int(game) <= len(games_list):
            print(f"You have chosen {games_list[int(game) - 1]}")
            game = int(game)
            break
        else:
            game = input("Choice must be a number between 1 and 3. Try again, or type 'q' to exit ")
            if game.lower() == 'q':
                return None

    difficulty = input("Please select your difficulty from 1 to 5: ")
    while True:
        if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
            difficulty = int(difficulty)
            break
        else:
            difficulty = input("Choice must be a number between 1 to 5. Try again, or type 'q' to exit: ")
            if difficulty.lower() == 'q':
                return None

    result = games_dict[game](difficulty)
    if result is True:
        score.add_score(difficulty)




