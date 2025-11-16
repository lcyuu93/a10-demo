# app/main.py

from app.calculator import add, subtract, multiply, divide
from app.storage import save_expenses_to_file, load_expenses_from_file


BANNER = "=== A10 DevSecOps Demo (Unsafe Calculator) ==="


def unsafe_calculate_expression(expr: str) -> float:
    """
    WARNING: This function is intentionally unsafe and uses eval()
    to demonstrate how SAST tools (e.g., Semgrep) can detect this pattern.
    """
    # DO NOT DO THIS IN REAL CODE.
    return eval(expr)  # noqa: S307


def main() -> None:
    print(BANNER)
    print("This demo keeps a very simple expense list and evaluates expressions.")
    expenses = load_expenses_from_file()

    while True:
        print("\nOptions:")
        print(" 1) Add expense")
        print(" 2) Show total (using safe calculator)")
        print(" 3) Evaluate custom expression (unsafe, uses eval)")
        print(" 4) Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            label = input("Expense label: ")
            amount_str = input("Amount: ")
            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount.")
                continue

            expenses.append({"label": label, "amount": amount})
            save_expenses_to_file(expenses)
            print(f"Added expense '{label}' = {amount}")

        elif choice == "2":
            total = 0.0
            for item in expenses:
                total = add(total, item.get("amount", 0.0))
            print(f"Total expenses = {total}")

        elif choice == "3":
            expr = input("Enter a Python expression to evaluate (e.g. 1+2*3): ")
            try:
                result = unsafe_calculate_expression(expr)
                print(f"Result = {result}")
            except Exception as e:  # noqa: BLE001 - intentionally broad
                print(f"Error evaluating expression: {e}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")