from brain_games.cli import welcome_user


# Engine for Brain Games.
def game_engine(game_description, question_generator):
    name = welcome_user()
    print(game_description)
    score = 0
    rounds = 3
    while score < rounds:
        question, correct = question_generator()
        print(f"Question: {question}")
        ans = input("Your answer: ").strip()
        if ans == str(correct):
            score += 1
            print("Correct!")
        else:
            score = 0
            print(f"'{ans}' is wrong answer. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
