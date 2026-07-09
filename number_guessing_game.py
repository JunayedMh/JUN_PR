import random

def chosee_difficulty():
    print("Choose difficulty:")
    print("1.Easy   (1-50,  10 attempts)")
    print("2.Medum   (1-100,  7 attempts)")
    print("3.Hard    (1-200   5 attempts)")

    while True:
        choice = input("Enter 1,2 or 3: ").strip()
        if choice == "1":
            return 1,50,10
        elif choice == "2":
            return 1,100,7
        elif choice == "3":
            return 1,200,5
        else:
            print("Select a valid option, Try again.")


def get_valid_guess(low,high):
    while True:
        input_value = input(f"Enter a number between {low} and {high}: ").strip()

        if not input_value.isdigit():
            print("Please enter a number:")
            continue

        guess = int(input_value)

        if guess < low or guess > high:
            print(f"Your guess must be in betweeen {low} and {high}, Try again.")
            continue

        return guess
    
def play_round(low,high,attempts):
    secret_num = random.randint(low,high)
    attempts_used = 0

    while attempts_used < attempts:
        remaining = attempts - attempts_used
        print(f"\nAttempts remaining: {remaining}")

        guess = get_valid_guess(low,high)
        attempts_used += 1

        if guess == secret_num:
            print(f"You have guessed the number: {secret_num}")
            print(f"You used {attempts_used} attempts.")
            return True
        elif guess < secret_num:
            print("Low")
        elif guess > secret_num:
            print("High")
        else:
            print("Error!")

    print(f"\nOut of attempts. The number was {secret_num}")
    return False

def main():
    print("====== Number Guessing Game ======")

    while True:
        low, high, attempts = chosee_difficulty()
        play_round(low,high,attempts)

        again = input("\nPlay again?(y/n): ").lower()
        if again == "n":
            print("Thanks for playing.")
            break

if __name__ == "__main__":
    main()
