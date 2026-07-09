import random,art

def play():
    print(art.guessing_game_logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1-100.")
    choice= input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    no=random.randint(1,100)

    if choice == "easy":
        attempts=10
    else:
        attempts=5

    for i in range(attempts):
        guess= int(input("Make a guess: "))
        if guess==no:
            print("You guessed the number!!")
            break
        else:
            attempts-=1

            print(f"Remaining attempts: {attempts}")
            if attempts>0:
                if guess<no:
                    print("Too low. \nGuess again")
                elif guess>no:
                    print("Too High. \nGuess again")
            elif attempts==0:
                print("You've run out of guesses. Refresh the page to run again.")

    if input("Do you want to play again? (y/n): ").lower()=="y":
        print("\n"*20)
        play()

play()
