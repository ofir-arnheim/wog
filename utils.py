import os


scores_file_name = "Scores.txt"
bad_return_code = ""


def screen_cleaner():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
