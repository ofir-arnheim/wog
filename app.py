import guess_game
import currency_roulette_game
import memory_game
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
def start_play():
    game = input("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
    guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    : """)
    games = ["Memory Game", "Guess Game", "Currency Roulette"]
    if game.isdigit() and 0 < int(game) <= len(games):
        print(f"You have chosen " + games[int(game)-1])
        if int(game) == 1:
            difficulty = input("Please select your difficulty from 1 to 5: ")
            if memory_game.play(difficulty) is True:
                score.add_score(difficulty)
        elif int(game) == 2:
            difficulty = input("Please select your difficulty from 1 to 100: ")
            if guess_game.play(difficulty) is True:
                score.add_score(difficulty)
        elif int(game) == 3:
            difficulty = input("Please select your difficulty from 1 to 10: ")
            if currency_roulette_game.play(difficulty) is True:
                score.add_score(difficulty)
    else:
        print("Choice must be a number between 1 and 3.")
