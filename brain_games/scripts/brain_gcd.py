from brain_games.scripts import user_greeting
from random import randint
import math
import prompt


def gcd():
    user_greeting
    print('Find the greatest common divisor of given numbers.')
    count = 0

    while count < 3:

        a = randint(1, 100)
        b = randint(1, 100)
        question = f"Question: {a}  {b}"
        correct = (math.gcd(a, b))
        print(question)
        user_answer = prompt.integer("Your answer: ")

        if user_answer == correct:
            print('Correct!')

        if count == 2 and user_answer == correct:

            print(f"Congratulations, {user_greeting.name}!")

        elif user_answer != correct:
            print(f"'{user_answer}' is wrong answer ;"
                  f"(. Correct answer was '{correct}'.")
            print(f"Let's try again, {user_greeting.name}!")
            break

        count = count + 1


def main():
    gcd()


if __name__ == '__main__':
    main()
