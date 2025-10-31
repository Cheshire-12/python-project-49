import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# We check whether it is a prime number or not.
def is_prime_number(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Question and correct answer generator for Prime game.
def generate_question():
    num = random.randint(1, 100)  # NOSONAR
    question = str(num)
    correct_answer = 'yes' if is_prime_number(num) else 'no'
    return question, correct_answer
