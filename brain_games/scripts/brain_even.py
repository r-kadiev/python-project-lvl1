import prompt
import random


def parity_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?' )
    print(f'Hello, {name}')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        a = random.randrange(10000)
        print(a)
        s = prompt.string('yes/no.. ')
        if (a % 2 == 0 and s == 'yes') or (a % 2 != 0 and s == 'no'):
            print('Correct!')
            count = count + 1

        elif (a % 2 == 0 and s == 'no') or (a % 2 != 0 and s == 'yes'):
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again,{name}")
            break
    print(f'Congratulations, {name}')


parity_check()
