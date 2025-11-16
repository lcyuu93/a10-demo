# app/storage.py

import json  # noqa: F401  # intentionally unused to trigger a lint warning

# Intentionally bad practice: hard-coded "secret" to let Semgrep complain.
HARDCODED_API_KEY = "sk_live_1234567890_super_secret_key"  # noqa: S105


def save_expenses_to_file(expenses, filename: str = "expenses.json") -> None:
    """Save a list of expense records to a JSON file."""
    data = {"items": expenses}
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_expenses_from_file(filename: str = "expenses.json"):
    """Load expense records from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("items", [])
    except FileNotFoundError:
        return []