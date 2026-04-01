import datetime
def read_history():
    try:
        with open("history.txy", "r" ) as file:
            return file.readlines()
    except FileNotFoundError:
        return[]
    
def save_transaction(trans_type, amount, category):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("history.txt", "a") as file:
        file.write(f"{date} | {trans_type} | ${amount:.2f} | {category}\n")

def calculate_balance():
    history = read_history()
    balance = 0.0
    for line in history:
        parts = line.split("|")
        trans_type = parts[1].strip()
        amount = float(parts[2].strip().replace('$', ''))
        if trans_type == "Income":
            balance += amount
        else:
            balance -= amount
    return balance

def run_app():
    while True:
        balance = calculate_balance()
        print(f"\n--- Wallet Dashboard | Balance: ${balance:.2f} ---")
        print("1. Add Income (+)")
        print("2. Add Expense (-)")
        print("3. View History")
        print("4. Exit")

        choice = input("Select: ")

        if choice in ["1", "2"]:
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                trans_type = "Income" if choice == "1" else "Expense"
                save_transaction(trans_type, amount, category)
                print(f"Success!")
            except ValueError:
                print("Error: Enter a valid number.")
        elif choice == "3":
            print("\n-- History ---")
            history = read_history()
            for record in history:
                print(record.strip())
        elif choice == "4":
            print("Googbye!")
            break

if __name__ == "__main__":
    run_app()