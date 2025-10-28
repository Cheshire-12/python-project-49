import random


# Brain Calculator Game.
def generate_expression():
    # Generate a random arithmetic expression.
    operators = ['+', '-', '*']
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operator = random.choice(operators)
    expression = f"{num1} {operator} {num2}"
    return expression


def get_user_name():
    # Get the user's name.
    return input("May I have your name? ")


def play_brain_calc():
    score = 0
    round = 3
    # Play the Brain Calculator game.
    print("Welcome to the Brain Games!")
    name = get_user_name()
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    
    # Game loop.
    while score < round:
        # Generate a random expression.
        expression = generate_expression()
        print(f"Question: {expression}")
        # Calculate the correct answer.
        correct_answer = eval(expression)
        # Check user input.
        while True:
            user_answer_str = input("Your answer: ").strip()
            if user_answer_str.lstrip('-').isdigit():
                user_answer_num = int(user_answer_str)
                user_answer = user_answer_num
                break
            else:
                print("Please enter a valid integer.")
        # Check if the answer is correct.
        if user_answer == correct_answer:
            score += 1
            print("Correct!")
        else:
            score = 0
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}")
    print(f"Congratulations, {name}!")