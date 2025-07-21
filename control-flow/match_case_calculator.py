# simple_calculator.py

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose operation (add, subtract, multiply, divide): ").lower()

        match operation:
            case "add":
                result = num1 + num2
                print(f"Result: {result}")
            case "subtract":
                result = num1 - num2
                print(f"Result: {result}")
            case "multiply":
                result = num1 * num2
                print(f"Result: {result}")
            case "divide":
                if num2 != 0:
                    result = num1 / num2
                    print(f"Result: {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            case _:
                print("Invalid operation. Please choose from: add, subtract, multiply, divide.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
