import csv
import os

FILE_PATH = "expenses.csv"

def create_file():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "note"])

def save_expense(date, category, amount, note):
    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])

def read_data():
    records = []
    if not os.path.exists(FILE_PATH):
        return records

    with open(FILE_PATH, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    return records