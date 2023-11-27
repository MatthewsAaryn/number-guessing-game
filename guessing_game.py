import random

scores = []

def min_score():
    high_score = scores[0]
    for score in scores:
        if score < high_score:
            high_score = score
    return high_score

def start_game():
    guess_counter = 1
    random_num = random.randrange(1, 101)
    if scores != []:
            print(f"\nYour high score is {min_score()} guesses!")

    while True:
        # Check the guess is valid
        try:
            guess = int((input("Please enter a number between 1 and 100: ")))
            if guess < 1 or guess > 100:
                print("Invalid guess, please only enter a number between 1 and 100.")
                continue
        except ValueError as err:
            print("Invalid guess, please enter a number between 1 and 100 using number keys.")
            continue
        # Check the guess against the random number
        if guess < random_num:
            print("It's higher. Please try again.")
            guess_counter += 1
            continue
        elif guess > random_num:
            print("It's lower. Please try again.")
            guess_counter += 1
            continue
        else:
            print(f"Congratulations, you guessed the correct number! It took you {guess_counter} guesses!")
            scores.append(guess_counter)
            break

    # Prompt the user to play again.        
    while True:
        prompt = input("Would you like to play again? Yes / No?: ")
        if prompt.lower() != "yes" and prompt.lower() != "no":
            print("Please enter only Yes or No.")
        elif prompt.lower() == "yes":
            start_game()
        else:
            print("\nThank you for playing!\n")
            quit()


welcome = "\n Welcome to the game!"
print(welcome)
print("*" * len(welcome))

start_game()
