import os

# Inventory structure: {ID: {"name": str, "price": float, "stock": int}}
inventory = {
    "101": {"name": "Laptop", "price": 75000, "stock": 10},
    "102": {"name": "Mouse", "price": 1500, "stock": 2}
}


def process_sale():
    p_id = input("Enter Product ID: ")
    if p_id in inventory:
        qty = int(input("Quantity:1 "))
        if inventory[p_id]['stock'] >= qty:
            total = inventory[p_id]['price'] * qty
            inventory[p_id]['stock'] -= qty

            # Generate Receipt File (Week 6 Concept)
            with open("receipt.txt", "w") as r:
                r.write(f"Product: {inventory[p_id]['name']}\nQty: {qty}\nTotal: {total}")
            print(f"Sale Successful! Total: {total}. Receipt generated.")
        else:
            print("Insufficient stock!")
    else:
        print("Product not found.")


def low_stock_report():
    print("\n--- Low Stock Alert (Below 5 units) ---")
    for pid, info in inventory.items():
        if info['stock'] < 5:
            print(f"ID: {pid} | {info['name']} | Remaining: {info['stock']}")


def main():
    while True:
        print("\n--- Inventory System ---")
        print("1. View Stock\n2. Process Sale\n3. Low Stock Report\n4. Exit")
        choice = input("Select: ")

        if choice == '1':
            for k, v in inventory.items():
                print(f"{k}: {v['name']} - ${v['price']} (Stock: {v['stock']})")
        elif choice == '2':
            process_sale()
        elif choice == '3':
            low_stock_report()
        elif choice == '4':
            break


if __name__ == "__main__":
    main()