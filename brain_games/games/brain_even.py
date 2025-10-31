import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


# Question and correct answer generator for Parity Check game.
def generate_question():
    number = random.randint(1, 100)  # NOSONAR
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer
