# multiplication_table.py

def multiplication_table():
    try:
        num = int(input("Enter a number: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

multiplication_table()
