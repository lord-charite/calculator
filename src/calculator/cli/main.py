from calculator.service.calculator import Calculator

"""Main entry point for the calculator application."""

def main() -> int:
    calc = Calculator()

    print("Simple Calculator")
    print("Commands: add, subtract, multiply, divide, exit")

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            return 0

        if command not in {"add", "subtract", "multiply", "divide"}:
            print("Invalid command")
            continue

        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
        except ValueError:
            print("Invalid number")
            continue

        try:
            if command == "add":
                result = calc.add(num1, num2)
            elif command == "subtract":
                result = calc.subtract(num1, num2)
            elif command == "multiply":
                result = calc.multiply(num1, num2)
            else:
                result = calc.divide(num1, num2)

            print(f"Result: {result}")

        except ZeroDivisionError:
            print("Cannot divide by zero")

if __name__ == "__main__":
    main()