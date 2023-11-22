import random

scores = []

def start_game():
    guess_counter = 1
    random_num = random.randrange(1, 101)

    while True:
        try:
            guess = int(input("Please enter a number between 1 and 100: "))
            if guess <= 0 or guess > 100:
                raise Exception("That guess is invalid, please try again: ")
        except ValueError:
            print("Please enter a number: ")
        except Exception as err:
            print(err)
        if guess < random_num:
            print("It's higher. Please try again: ")
            guess_counter += 1
        elif guess > random_num:
            print("It's lower. Please try again: ")
            guess_counter += 1
        else:
            print(f"Congratulations, you guessed the correct number! It took you {guess_counter} tries!")
            scores.append(guess_counter)
            print(f"Your high score is {min(scores)}!")
            break

    while True:
        prompt = input("Would you like to play again? Yes / No?: ")
        if prompt.lower() != "yes" and prompt.lower() != "no":
            print("Please enter only Yes or No.")
            continue
        elif prompt.lower() == "yes":
            start_game()
        else:
            print("\nThank you for playing!\n")
            quit()


welcome = "\n Welcome to the game!"
print(welcome)
print("*" * len(welcome))

start_game()
