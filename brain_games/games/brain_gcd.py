import math
import random

# Brain Greatest common divisor (GCD) game.
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


# Question and correct answer generator for GCD game.
def generate_question():
    num1 = random.randint(1, 100) #NOSONAR
    num2 = random.randint(1, 100) #NOSONAR
    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
