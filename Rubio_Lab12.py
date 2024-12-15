def show_menu():
    print("\n--- Food Menu ---")
    print("1. Burger - ₱99.00")
    print("2. Pizza - ₱495.00")
    print("3. Chicken Meal - ₱333.00")
    print("4. Salad - ₱275.00")
    print("5. Beverage - ₱110.00")
    print("6. Pasta - ₱213.00")

def choose_item():
    while True:
        try:
            choice = int(input("\nEnter the number of the item you'd like to order: "))
            if choice == 1:
                return "Burger", 99.00
            elif choice == 2:
                return "Pizza", 495.00
            elif choice == 3:
                return "Chicken Meal", 333.00
            elif choice == 4:
                return "Salad", 275.00
            elif choice == 5:
                return "Beverage", 110.00
            elif choice == 6:
                return "Pasta", 213.00
            else:
                print("Invalid choice. Please choose a valid menu item.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def take_payment(total_cost):
    while True:
        try:
            cash = float(input(f"\nTotal cost is ₱{total_cost:.2f}. Enter payment amount: "))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment accepted. Your change is ₱{change:.2f}.")
                break
            else:
                print(f"Insufficient payment. You are short by ₱{total_cost - cash:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    show_menu()
    item_name, item_price = choose_item()
    print(f"You selected: {item_name} - ₱{item_price:.2f}")
    take_payment(item_price)
    print("\nThank you for your order!")

if __name__ == "__main__":
    main()
