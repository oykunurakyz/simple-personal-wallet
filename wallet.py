import datetime
import matplotlib.pyplot as plt

def read_history():
    try:
        with open("history.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_transaction(trans_type, amount, category):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("history.txt", "a") as file:
        file.write(f"{date} | {trans_type} | ${amount:.2f} | {category}\n")

def calculate_balance():
    history = read_history()
    balance = 0.0
    for line in history:
        parts = line.split("|")
        if len(parts) < 4: continue
        trans_type = parts[1].strip()
        amount = float(parts[2].strip().replace('$', ''))
        if trans_type == "Income":
            balance += amount
        else:
            balance -= amount
    return balance

def show_chart():
    history = read_history()
    categories = {}
    for line in history:
        parts = line.split("|")
        if len(parts) < 4: continue
        trans_type = parts[1].strip()
        amount = float(parts[2].strip().replace('$', ''))
        category = parts[3].strip()
        if trans_type == "Expense":
            categories[category] = categories.get(category, 0) + amount
            
    if not categories:
        print("\n[!] No expenses to show in chart.")
        return

    plt.figure(figsize=(8, 6))
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

def run_app():
    while True:
        balance = calculate_balance()
        print(f"\n--- Balance: ${balance:.2f} ---")
        print("1. Income | 2. Expense | 3. History | 4. Chart | 5. Exit")
        choice = input("Select: ")
        if choice in ["1", "2"]:
            amount = float(input("Amount: "))
            category = input("Category: ")
            save_transaction("Income" if choice == "1" else "Expense", amount, category)
        elif choice == "3":
            for r in read_history(): print(r.strip())
        elif choice == "4":
            show_chart()
        elif choice == "5":
            break

if __name__ == "__main__":
    run_app()
