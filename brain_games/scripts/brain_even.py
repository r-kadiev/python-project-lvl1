import prompt
import random


def parity_check():
    global s
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        a = random.randrange(10000)
        print(f'Question: {int(a)}')
        s = prompt.string('Your answer: ')
        if (a % 2 == 0 and s == 'yes') or (a % 2 != 0 and s == 'no'):
            print('Correct!')
            count = count + 1
            if count == 3:
                print(f'Congratulations, {name}')

        elif (a % 2 == 0 and s == 'no') or (a % 2 != 0 and s == 'yes'):
            print(f" '{s}'  is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}")
            break
        elif s!='no' or s!='yes':
            print('Вы ввели неправильный формат ответа! ')
            break


parity_check()


