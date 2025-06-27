from importlib.metadata import PackageNotFoundError


def user_guessing_game(secret_num, stop_chars):
    user_input = ''
    while user_input != stop_chars:
        user_input = input("\nGuess a number from 1 to 100: ")
        if user_input == secret_num:
            print("BINGO!!")
        else:
         print(f"The number is {user_input}. Try again.")
#user_guessing_game(str(15), "stop")

name = "já"

class Test:
    a = 55