from random import randint
import math
import prompt
from brain_games.scripts import user_greeting

user_greeting
print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(num):
    mx = math.sqrt(num)

    i = 2
    while i <= mx:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def run_game():
    count = 0
    while count < 3:

        question = randint(0, 100)
        prime = 'yes' if is_prime(question) else 'no'
        print(f'Question: {question}')
        s = prompt.string('Your answer: ')
        if s == prime:
            print('Correct!')
            count = count + 1
            if count == 3:
                print(f"Congratulations, {user_greeting.name}!")
        else:
            print(f"'{s}' is wrong answer ;(. Correct answer was '{prime}'.")
            print(f"Let's try again, {user_greeting.name}!")
            break


def main():
    run_game()


if __name__ == '__main__':
    main()
