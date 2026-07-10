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

def km_to_miles(value):
    return value * 0.621371

def miles_to_km(value):
    return value / 0.621371

def kg_to_lbs(value):
    return value * 2.20462

def lbs_to_kg(value):
    return value / 2.20462

def celsius_to_fahrenheit(value):
    return (value *9/5) +32

def fahrenheit_to_celsius(value):
    return (value -32) * 5/9

CONVERSIONS = {
    "1": ("Kilometers to Miles", km_to_miles),
    "2": ("Miles to Kilometers", miles_to_km),
    "3": ("Kilograms to pound", kg_to_lbs),
    "4": ("Pounds to kilograms", lbs_to_kg),
    "5": ("Celsius to fahrenheit", celsius_to_fahrenheit),
    "6": ("Fahrenheit to Celsius", fahrenheit_to_celsius)
}

def run_converter():
    print("\n--- Unit Converter ---")
    for key, (label, _) in CONVERSIONS.items():
        print(f"{key}. {label}")

    choice = input(f"Choose a conversion (1-{len(CONVERSIONS)}): ").strip()

    if choice not in CONVERSIONS:
        print("Invalid choice.")
        return
        
    label,conversion_function = CONVERSIONS[choice]
    value = get_number("Enter the value to convert: ")
    result = conversion_function(value)
    print(f"{label}: {value} -> {result:.4f}")


def main():

    print("====== Calculator ======")
    while True:
        print("\n1.Calculator")
        print("2.Unit Converter")
        print("3.Exit")


        choice = input("Chose an option (1-3): ").strip()

        if choice == "1":
            run_calc()
        elif choice == "2":
            run_converter()
        elif choice == "3":
            print("Thanks for using calculator.")
            break
        else:
            print("Invalid choice. Try again")


if __name__ == "__main__":
    main()