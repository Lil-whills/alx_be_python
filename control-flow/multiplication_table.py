

def multiplication_table():

try:
    num = int(input("Enter a number to see its multiplication table:"))
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
except ValueError:
    print("Please enter a valid number.")


multiplication_table()
