import random

DESCRIPTION = "What number is missing in the progression?"


# Question and correct answer generator for Brain Progression game.
def question_generator():
    progression_length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    hidden_index = random.randint(1, progression_length - 2)

    progression = [str(start + i * step) for i in range(progression_length)]
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    question = ' '.join(progression)
    return question, correct_answer