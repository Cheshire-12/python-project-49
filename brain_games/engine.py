from brain_games.cli import welcome_user


# Engine for Brain Games.
def game_engine(game_description, question_generator):
    name = welcome_user()
    print(game_description)
    score = 0
    rounds = 3
    while score < rounds:
        question, correct_answer = question_generator()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        if user_answer == str(correct_answer):
            score += 1
            print("Correct!")
        else:
            score = 0
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")
