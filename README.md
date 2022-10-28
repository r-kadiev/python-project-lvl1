### Hexlet tests and linter status:
[![Actions Status](https://github.com/r-kadiev/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/r-kadiev/python-project-lvl1/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/e7c1a9e524deda32f093/maintainability)](https://codeclimate.com/github/r-kadiev/python-project-lvl1/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e7c1a9e524deda32f093/test_coverage)](https://codeclimate.com/github/r-kadiev/python-project-lvl1/test_coverage)




### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |
| [wemake-python-styleguide](https://wemake-python-stylegui.de)               | "the strictest and most opinionated python linter ever" |

---
## Install
```
git clone https://github.com/r-kadiev/python-project-lvl1
cd python-project-lvl1
make package-install
```

## `Usage`
* Even number: `brain-even`
* Calculate the expression: `brain-calc`
* Greatest common divisor: `brain-gcd`
* Guess missing number: `brain-progression`
* Prime number: `brain-prime`

## Description


### Игра: "Проверка на чётность"
Суть игры в следующем: пользователю показывается случайное число. 
И ему нужно ответить yes, если число чётное, или no — если нечётное:
[![asciicast](https://asciinema.org/a/533058.svg)](https://asciinema.org/a/533058)


### Игра: "Калькулятор"
Суть игры в следующем: пользователю показывается случайное математическое выражение,
например 35 + 16,
которое нужно вычислить и записать правильный ответ.
[![asciicast](https://asciinema.org/a/533052.svg)](https://asciinema.org/a/533052)


### Игра: "НОД" 
Суть игры в следующем: пользователю показывается два случайных числа, например, 25 50. 
Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
[![asciicast](https://asciinema.org/a/533059.svg)](https://asciinema.org/a/533059)

### Игра: "Арифметическая прогрессия"
Показываем игроку ряд чисел, образующий арифметическую прогрессию, заменив любое из чисел двумя точками.
Игрок должен определить это число.
[![asciicast](https://asciinema.org/a/533062.svg)](https://asciinema.org/a/533062)

### Игра "Простое ли число?"
Пользователю нужно угадать простое ли число.
[![asciicast](https://asciinema.org/a/533064.svg)](https://asciinema.org/a/533064)