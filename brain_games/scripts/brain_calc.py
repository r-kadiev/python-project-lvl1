import prompt
from random import randint, choice
from operator import add, sub, mul
from brain_games.scripts import user_greeting


OPERATIONS = [("+", add), ("-", sub), ("*", mul)]


def calc():
    user_greeting
    rules = "What is the result of the expression?"
    print(rules)
    count = 0

    while count < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        operator, func = choice(OPERATIONS)
        question = f"Question: {a} {operator} {b}"
        correct = func(a, b)
        print(question)
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(correct):
            print('Correct!')
            count = count + 1

            if count == 3:
                print(f'Congratulations, {user_greeting.name}!')
                break
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{str(correct)}'.")
            break


def main():
    calc()


if __name__ == '__main__':
    main()
