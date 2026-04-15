from datetime import datetime
from storage import create_file, save_expense, read_data
from report import monthly_report
from charts import draw_pie_chart

def run():
    create_file()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View monthly report")
        print("3. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            date = input("Date (YYYY-MM-DD, leave blank for today): ").strip()
            if not date:
                date = datetime.today().strftime("%Y-%m-%d")

            category = input("Category: ").strip()
            amount = input("Amount: ").strip()
            note = input("Note: ").strip()

            try:
                amount = float(amount)
                save_expense(date, category, amount, note)
                print("Saved successfully.")
            except ValueError:
                print("Invalid amount. Try again.")

        elif option == "2":
            month = input("Enter month (YYYY-MM): ").strip()
            data = read_data()

            summary = monthly_report(data, month)

            if not summary:
                print("No records found.")
                continue

            total, category_data, top_category = summary

            print(f"\nTotal spent: ₹{round(total, 2)}")
            print("\nBy category:")
            for cat, amt in category_data.items():
                print(f"{cat}: ₹{round(amt, 2)}")

            print(f"\nTop spending category: {top_category}")

            show = input("Show chart? (y/n): ").strip().lower()
            if show == "y":
                draw_pie_chart(category_data, month)

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

run()