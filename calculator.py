
# Interactive Calculator & Unit Converter

# Conversion factors are kept in one place.
CONVERSIONS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462,
}


# Read a number safely. Repeat until the input is valid.
def read_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number, such as 12 or 3.5.")


# Arithmetic operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Unit conversions
def km_to_miles(km):
    return km * CONVERSIONS["km_to_miles"]


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def kg_to_pounds(kg):
    return kg * CONVERSIONS["kg_to_pounds"]


# Display and handle the unit-conversion menu.
def convert_units():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometres to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "4":
            return

        if choice not in ("1", "2", "3"):
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue

        value = read_number("Enter the value to convert: ")

        if choice == "1":
            print(f"{value:g} km = {km_to_miles(value):.4f} miles")
        elif choice == "2":
            print(
                f"{value:g} C = "
                f"{celsius_to_fahrenheit(value):.2f} F"
            )
        else:
            print(f"{value:g} kg = {kg_to_pounds(value):.4f} pounds")


# Main menu
def main():
    while True:
        print("\n=== Interactive Calculator & Unit Converter ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Convert Units")
        print("6. Quit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "6":
            print("Goodbye!")
            break

        if choice == "5":
            convert_units()
            continue

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select a number from 1 to 6.")
            continue

        first = read_number("Enter the first number: ")
        second = read_number("Enter the second number: ")

        if choice == "1":
            result = add(first, second)
        elif choice == "2":
            result = subtract(first, second)
        elif choice == "3":
            result = multiply(first, second)
        else:
            result = divide(first, second)

        if isinstance(result, (int, float)):
            print(f"Result: {result:g}")
        else:
            print(result)


if __name__ == "__main__":
    main()
