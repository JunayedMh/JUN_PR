def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError("Can't divide by zero")
    return a / b

def get_number(num):
    while True:
        input_value = input(num).strip()
        try:
            return float(input_value)
        except ValueError:
            print("Please enter a valid number.")

def run_calc():
    print("\n--- Calculator ---")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")

    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide)
    }

    choice = input("Choose an operaton (1-4): ").strip()

    if choice not in operations:
        print("Invalid choice.")
        return
    
    label, operation_fuction = operations[choice]

    first_num = get_number("Enter the first number: ")
    second_num = get_number("Enter the second number: ")

    try:
        result = operation_fuction(first_num, second_num)
        print(f"{label} result: {result}")
    except ValueError as error:
        print(f"Error: {error}")


def main():

    print("====== Calculator ======")
    while True:
        print("\n1.Calculator")
        print("2.EXit")

        choice = input("Chose an option (1-3): ").strip()

        if choice == "1":
            run_calc()
        elif choice == "2":
            print("ok")
            break
        else:
            print()

if __name__ == "__main__":
    main()