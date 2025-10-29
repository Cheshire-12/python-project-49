import operator
import random

# Description for the Calc game.
DESCRIPTION = 'What is the result of the expression?'


# Question and correct answer generator for Calc game.
def generate_question():
    ops = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul
                 }
    ops_symbols = random.choice(list(ops.keys()))
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operator_func = ops[ops_symbols]
    question = f"{num1} {ops_symbols} {num2}"
    correct_answer = operator_func(num1, num2)
    return question, correct_answer
