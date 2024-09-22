# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))

def display_products(products_list):
    for index, (name, price) in enumerate(products_list, start=1):
        print(f"{index}. {name} - ${price}")

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    for name, price, quantity in cart:
        item_cost = price * quantity
        total_cost += item_cost
        print(f"{name} - ${price} x {quantity} = ${item_cost}")
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product in cart:
        print(f"{product[2]} x {product[0]} - ${product[1]} = ${product[1] * product[2]}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email and len(email.strip()) > 0

def main():
    cart = []
    
    # Get user name
    while True:
        name = input("Enter your name (first and last): ")
        if validate_name(name):
            break
        print("Invalid name. Please enter a valid name.")

    # Get user email
    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email.")

    while True:
        display_categories()
        category_choice = input("Select a category by number: ")
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(products):
            category_index = int(category_choice) - 1
            category = list(products.keys())[category_index]
            products_list = products[category]
            break
        print("Invalid category selection. Please try again.")

    while True:
        display_products(products_list)
        print("Options:")
        print("1. Select a product to buy")
        print("2. Sort the products by price")
        print("3. Go back to the category selection")
        print("4. Finish shopping")
        
        option = input("Choose an option (1-4): ")

        if option == '1':
            product_choice = input("Select a product by number: ")
            if product_choice.isdigit() and 1 <= int(product_choice) <= len(products_list):
                product_index = int(product_choice) - 1
                selected_product = products_list[product_index]
                while True:
                    quantity = input("Enter quantity: ")
                    if quantity.isdigit() and int(quantity) > 0:
                        add_to_cart(cart, selected_product, int(quantity))
                        print(f"Added {quantity} x {selected_product[0]} to cart.")
                        break
                    print("Invalid quantity. Please enter a positive number.")
            else:
                print("Invalid product selection.")

        elif option == '2':
            sort_order = input("Sort by price: 1 for ascending, 2 for descending: ")
            if sort_order in ['1', '2']:
                order = "asc" if sort_order == '1' else "desc"
                sorted_products = display_sorted_products(products_list, order)
                display_products(sorted_products)
            else:
                print("Invalid input. Please try again.")

        elif option == '3':
            main()

        elif option == '4':
            if cart:
                total_cost = display_cart(cart)
                address = input("Enter delivery address: ")
                generate_receipt(name, email, cart, total_cost, address)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
