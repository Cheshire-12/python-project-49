import random


# Brain Even Game
def is_even(number):
    # Check if a number is even.
    return number % 2 == 0


def get_user_name():
    # Get the user's name.
    return input("May I have your name? ")


def play_brain_even():
    score = 0
    rounds = 3
    # Play the Brain Even game.
    print("Welcome to the Brain Games!")
    name = get_user_name()
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    # Game loop
    while score < rounds:
        # Generate a random number
        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        # Get user input
        user_answer = input("Your answer: ").strip().lower()

        # Check if the answer is correct
        if (is_even(number) and user_answer == "yes") or (not is_even(number) and user_answer == "no"):
            score += 1
            print("Correct!")
        else:
            score = 0
            print("Wrong answer. Let's try again!")
    print(f"Congratulations, {name}!")
