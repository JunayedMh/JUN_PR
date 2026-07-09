# Number Guessing Game

A command line number guessing game written in Python. The computer picks a random number
within a range you choose, and you have a limited number of attempts to guess it, with
"too high" / "too low" feedback after each guess.

## Features

- Three difficulty levels, each with a different range and attempt limit
  - Easy: 1-50, 10 attempts
  - Medium: 1-100, 7 attempts
  - Hard: 1-200, 5 attempts
- Input validation: rejects non-numeric input and out-of-range guesses without crashing
- Replay loop: play multiple rounds without restarting the program

## Requirements

- Python 3.6 or newer
- No external libraries. Only the Python standard library (`random`) is used.

## How to run

```bash
python number_guessing_game.py
```

or on some systems:

```bash
python3 number_guessing_game.py
```

## Example

```
=== Number Guessing Game ===
Choose a difficulty:
1. Easy   (1-50,  10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard   (1-200, 5 attempts)
Enter 1, 2, or 3: 2

Attempts remaining: 7
Enter a number between 1 and 100: 50
Too high.

Attempts remaining: 6
Enter a number between 1 and 100: 25
Too low.

Attempts remaining: 5
Enter a number between 1 and 100: 37
Correct. The number was 37.
You used 3 attempt(s).

Play again? (y/n):
```

## What this project covers

Written as a beginner exercise focused on core fundamentals: `while` loops, `if/elif/else`
branching, functions with parameters and multiple return values, basic input validation,
and the `random` module.
