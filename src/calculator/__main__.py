from calculator import Calculator

"""Main entry point for the calculator application."""

def main():
    """Run the calculator in interactive mode."""
    calc = Calculator()
    print("Simple Calculator")
    print("Commands: add, subtract, multiply, divide, clear, exit")
    
    while True:
        try:
            command = input("\nEnter command: ").strip().lower()
            
            if command == "exit":
                print("Goodbye!")
                break
            elif command == "clear":
                calc.clear()
                print("Calculator cleared")
            elif command in ["add", "subtract", "multiply", "divide"]:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))
                
                if command == "add":
                    result = calc.add(num1, num2)
                elif command == "subtract":
                    result = calc.subtract(num1, num2)
                elif command == "multiply":
                    result = calc.multiply(num1, num2)
                else:  # divide
                    result = calc.divide(num1, num2)
                
                print(f"Result: {result}")
            else:
                print("Invalid command")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except ZeroDivisionError:
            print("Error: Division by zero")


if __name__ == "__main__":
    main()