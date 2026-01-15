def main():
    print("Welcome to the Budget Tracker!")
    initial_budget = float(input("Enter your initial budget: "))

    budget = initial_budget
    expenses = []

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Remaining Budget")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            expense_name = input("Enter expense name: ")
            expense_amount = float(input("Enter expense amount: "))
            if expense_amount > budget:
                print("Insufficient budget for this expense.")
            else:
                expenses.append((expense_name, expense_amount))
                budget -= expense_amount
                print(f"Expense '{expense_name}' of amount {expense_amount} added.")
        elif choice == '2':
            if not expenses:
                print("No expenses recorded.")
            else:
                print("\nExpenses:")
                for name, amount in expenses:
                    print(f"- {name}: {amount}")
                print(f"Total expenses: {initial_budget - budget}")
        elif choice == '3':
            print(f"Remaining budget: {budget}")
        elif choice == '4':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
