#how insert argument to the function. "name" is argument. "Hello" is argument.
#def greeting_9(name):
#    print(name)

#greeting_9("Hi")

def user_guessing_game(secret_num, stop_character):
    user_input = ''
    while user_input != stop_character:
        user_input = input("\nGuess a number from 1 to 100: ")
        if user_input == secret_num:
            print("BINGO!!")
    else:
        print(f"The number is {user_input}. Try again.")

#user_guessing_game(str(1), "stop")

#How to return item from the function
#def sum_of(a: int, b: int):
#    return a + b, a * b
#c, d = sum_of(3, 2)
#print(c)
#print(d)
a = 'hi'
a = 45
def sum_of(a: int, b: int) -> int:
    return a + b

c = sum_of(25, 5)
print(c)
