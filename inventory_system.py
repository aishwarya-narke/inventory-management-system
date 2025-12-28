inventory = []

while True:
    print("\n1. Add Product")
    print("2. Sell Product")
    print("3. Show Inventory")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter product name: ").strip().lower()

        while True:
            try:
                qty = int(input("Enter quantity: "))
                if qty <= 0:
                    print("Quantity must be greater than zero.")
                else:
                    break
            except ValueError:
                print("Enter a valid number.")

        for item in inventory:
            if item["name"] == name:
                item["quantity"] += qty
                print("Product updated successfully.")
                break
        else:
            inventory.append({"name": name, "quantity": qty})
            print("Product added successfully.")

    elif choice == "2":
        name = input("Enter product name to sell: ").strip().lower()

        try:
            sell_qty = int(input("Enter quantity to sell: "))
            if sell_qty <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Invalid quantity.")
            continue

        for item in inventory:
            if item["name"] == name:
                if sell_qty > item["quantity"]:
                    print("Not enough stock.")
                else:
                    item["quantity"] -= sell_qty
                    if item["quantity"] == 0:
                        inventory.remove(item)
                        print("Sale successful. Product is now out of stock.")
                    else:
                        print("Sale successful.")
                break
        else:
            print("Product not found.")

    elif choice == "3":
        if not inventory:
            print("\nInventory is empty.")
        else:
            print("\nInventory:")
            for item in inventory:
                print(item["name"].title(), "-", item["quantity"])

    elif choice == "4":
        print("Exiting system.")
        break

    else:
        print("Invalid option. Choose 1-4.")