def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
