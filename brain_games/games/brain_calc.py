import operator
import random

# Description for the Calc game.
DESCRIPTION = 'What is the result of the expression?'


# Question and correct answer generator for Calc game.
def generate_question():
    operations = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul
                 }
    op_symbol = random.choice(list(operations.keys())) #NOSONAR
    num1 = random.randint(1, 25) #NOSONAR
    num2 = random.randint(1, 25) #NOSONAR
    operator_func = operations[op_symbol]
    question = f"{num1} {op_symbol} {num2}"
    correct_answer = operator_func(num1, num2)
    return question, correct_answer
