# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_SUBTRACT = 32
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_TO_CELSIUS_SUBTRACT

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_SUBTRACT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def display_menu():
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            temp = float(input("Enter temperature in Celsius: "))
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.2f}°F")
        elif choice == '2':
            temp = float(input("Enter temperature in Fahrenheit: "))
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is {result:.2f}°C")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
