import csv
import math
from tabulate import tabulate

FILE = "fitness_data.csv"
FIELDS = ["ID", "Name", "Age", "Workout", "Duration", "Calories", "HR", "Steps"]


def load_data():
    with open(FILE, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_data(data):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)


def _prompt_required(prompt, previous_field=None):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        if previous_field:
            print(f'Please fill the previous entry "{previous_field}" first.')
        else:
            print("This field is required.")


def _prompt_number(prompt, integer=False, previous_field=None):
    while True:
        value = _prompt_required(prompt, previous_field)
        try:
            number = float(value)
            if not math.isfinite(number) or number < 0 or (integer and not number.is_integer()):
                raise ValueError
            return str(int(number)) if integer else str(number)
        except ValueError:
            kind = "a non-negative integer" if integer else "a non-negative number"
            print(f"Enter {kind}.")


def display_all():
    data = load_data()
    print(tabulate(data, headers="keys", tablefmt="grid"))
    print(f"Total records: {len(data)}")


def add_record():
    data = load_data()
    while True:
        record_id = _prompt_required("ID: ").upper()
        if any(record["ID"].strip().upper() == record_id for record in data):
            print("That ID already exists. Enter a unique ID.")
            continue
        break

    data.append({
        "ID": record_id,
        "Name": _prompt_required("Name: ", previous_field="ID"),
        "Age": _prompt_number("Age: ", integer=True, previous_field="Name"),
        "Workout": _prompt_required("Workout: ", previous_field="Age"),
        "Duration": _prompt_number("Duration (mins): ", integer=True, previous_field="Workout"),
        "Calories": _prompt_number("Calories: ", previous_field="Duration"),
        "HR": _prompt_number("Avg HR: ", integer=True, previous_field="Calories"),
        "Steps": _prompt_number("Steps: ", integer=True, previous_field="HR")
    })
    save_data(data)
    print("Record added!")


def search_record():
    q = input("Search ID or Name: ").strip().lower()
    matches = [r for r in load_data() if q in r["ID"].lower() or q in r["Name"].lower()]
    if matches:
        print(tabulate(matches, headers="keys", tablefmt="grid"))
    else:
        print("No record found.")


def update_record():
    rid = input("Enter ID to update: ").strip().upper()
    data = load_data()
    for r in data:
        if r["ID"] == rid:
            new_cal = input(f"New Calories [{r['Calories']}]: ").strip()
            if new_cal:
                r["Calories"] = new_cal
            save_data(data)
            print("Updated!")
            return
    print("ID not found.")


def delete_record():
    rid = input("Enter ID to delete: ").strip().upper()
    data = load_data()
    filtered = [r for r in data if r["ID"] != rid]
    if len(filtered) < len(data):
        save_data(filtered)
        print("Deleted!")
    else:
        print("ID not found.")