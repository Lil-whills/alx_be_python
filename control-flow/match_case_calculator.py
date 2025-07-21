# match_case_calculator.py

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")

        match operation:
            case "+":
                print(f"Result: {num1 + num2}")
            case "-":
                print(f"Result: {num1 - num2}")
            case "*":
                print(f"Result: {num1 * num2}")
            case "/":
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
            case _:
                print("Invalid operation. Please choose one of: +, -, *, /.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()
