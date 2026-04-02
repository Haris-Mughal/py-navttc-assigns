import os


def load_data():
    expenses = {}
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as f:
            for line in f:
                cat, amt = line.strip().split(",")
                expenses[cat] = expenses.get(cat, 0) + float(amt)
    return expenses


def save_data(category, amount):
    with open("expenses.txt", "a") as f:
        f.write(f"{category},{amount}\n")


def main():
    budget = 5000.0
    expenses = load_data()

    while True:
        print("\n--- Smart Expense Tracker ---")
        print(f"Current Budget: {budget} | Total Spent: {sum(expenses.values())}")
        print("1. Add Expense\n2. View Summary\n3. Exit")
        choice = input("Select: ")

        if choice == '1':
            cat = input("Category (Food/Travel/Bills): ")
            amt = float(input("Amount: "))
            expenses[cat] = expenses.get(cat, 0) + amt
            save_data(cat, amt)
            if sum(expenses.values()) > budget:
                print("⚠️ WARNING: You have exceeded your budget!")
        elif choice == '2':
            for c, a in expenses.items():
                print(f"{c}: {a}")
            if expenses:
                top = max(expenses, key=expenses.get)
                print(f"Highest Spending Category: {top}")
        elif choice == '3':
            break


if __name__ == "__main__":
    main()