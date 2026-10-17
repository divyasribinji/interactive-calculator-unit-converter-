
# Interactive Calculator and Unit Converter

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculator():
    print("\n--- Basic Calculator ---")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Choose an operation (1-4): ")
        if choice in ("1", "2", "3", "4"):
            break
        print("Invalid choice! Enter 1, 2, 3, or 4.")

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    while True:
        choice = input("Choose conversion (1-2): ")
        if choice in ("1", "2"):
            break
        print("Invalid choice! Enter 1 or 2.")

    value = get_number("Enter the value: ")

    if choice == "1":
        result = value * 0.621371
        print(value, "kilometers =", round(result, 2), "miles")
    else:
        result = (value * 9 / 5) + 32
        print(value, "Celsius =", round(result, 2),
              "Fahrenheit")


def currency_converter():
    print("\n--- Currency Converter ---")
    print("1. INR to USD")
    print("2. USD to INR")
    print("Demo exchange rate: 1 USD = 85 INR")

    while True:
        choice = input("Choose conversion (1-2): ")
        if choice in ("1", "2"):
            break
        print("Invalid choice! Enter 1 or 2.")

    amount = get_number("Enter amount: ")

    if amount < 0:
        print("Amount cannot be negative.")
    elif choice == "1":
        print("Converted amount:", round(amount / 85, 2), "USD")
    else:
        print("Converted amount:", round(amount * 85, 2), "INR")


def main():
    while True:
        print("\n==============================")
        print(" INTERACTIVE CALCULATOR")
        print("      UNIT CONVERTER")
        print("==============================")
        print("1. Basic Calculator")
        print("2. Unit Converter")
        print("3. Currency Converter")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            currency_converter()
        elif choice == "4":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
