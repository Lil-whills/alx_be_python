#!/usr/bin/env python3

# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    while True:
        try:
            temp_input = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                converted = celsius_to_fahrenheit(temp_input)
                print(f"{temp_input}°C is {converted:.2f}°F\n")
            elif unit == 'F':
                converted = fahrenheit_to_celsius(temp_input)
                print(f"{temp_input}°F is {converted:.2f}°C\n")
            else:
                print("Invalid unit. Please enter C or F.\n")
                continue

            again = input("Do you want to convert another temperature? (y/n): ").strip().lower()
            if again != 'y':
                print("Exiting the Temperature Conversion Tool.")
                break

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
