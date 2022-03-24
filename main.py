from random import randint
from logo import art
EASY_LEVEL = 10
HARD_LEVEL = 5

def check(guess, answer, attempts):
    """"it checks number against guess, return number of remaining """
    if guess > answer:
        print("HIGH !!!")
        return attempts - 1
    elif guess < answer:
        print("LOW !!!")
        return attempts - 1
    else:
        print(f"CONGRATULATIONS!,YOU GOT THE CORRECT ANSWER {answer}.")

def difficulty():
    level = input("Choose EASY level or HARD level :").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(art)
    print("WELCOME TO NUMBER GUESSING GAME,\nYou have to guess number only between 1 to 100.")
    answer = randint(1, 100)
    # print(f"final answer is {answer}.")
    attempts = difficulty()
    guess = 0
    while guess != answer:
        print(f"You have >{attempts}< attempts.")
        guess = int(input("Guess the number : "))
        attempts = check(guess, answer, attempts)
        if attempts == 0:
            print("YOU 'VE RUN OUT OF GUESSES, BETTER LUCK NEXT TIME.")
            return
        elif guess != answer:
            print(">>> GUESS AGAIN <<<")
game()