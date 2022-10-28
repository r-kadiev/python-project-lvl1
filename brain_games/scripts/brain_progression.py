import prompt
from random import randint
from brain_games.scripts import user_greeting

user_greeting
RULES = "What number is missing in the progression?"
print(RULES)


def generate_progression():
    step = randint(1, 10)
    start = randint(1, 100)
    stop = start + (step * 10)
    progression = [str(x) for x in range(start, stop, step)]
    return progression


def run_game():
    count = 0
    while count < 3:
        progression = generate_progression()

        skip = randint(0, 9)
        correct = progression[skip]

        progression[skip] = ".."
        question = " ".join(progression)

        print(f"Question: {question}")
        s = prompt.string('Your answer: ')

        if s == correct:
            print('Correct!')
            count = count + 1
            if count == 3:
                print(f"Congratulations, {user_greeting.name}!")
        else:
            print(f"'{s}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {user_greeting.name}!")
            break


def main():
    run_game()


if __name__ == '__main__':
    main()
