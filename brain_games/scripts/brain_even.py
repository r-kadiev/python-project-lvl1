import prompt
import random
from brain_games.scripts import user_greeting

answer_yes = 'yes'
answer_no = 'no'


def even():

    user_greeting
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        question = random.randrange(100)
        print(f'Question: {int(question)}')
        s = prompt.string('Your answer: ')
        count = count + 1

        if count == 3:
            print('Correct!')
            print(f'Congratulations, {user_greeting.name}!')
            break

        if question % 2 == 0:
            answer = 'yes'

            if s == answer_yes:
                print('Correct!')
            else:
                print(f"'{s}' is wrong answer ;(. "
                      f"Correct answer was '{answer}'.")
                print(f"Let's try again, {user_greeting.name}!")
                break

        if question % 2 != 0:
            answer = 'no'

            if s == answer_no:
                print('Correct!')
            else:
                print(f"'{s}' is wrong answer ;(."
                      f" Correct answer was '{answer}'.")
                print(f"Let's try again, {user_greeting.name}!")
                break


def main():
    even()


if __name__ == '__main__':
    main()
