import matplotlib.pyplot as plt

def draw_pie_chart(category_data, month):
    labels = list(category_data.keys())
    values = list(category_data.values())
    total = sum(values)

    def format_label(pct):
        amount = (pct / 100) * total
        return f"{pct:.1f}%\n₹{amount:.0f}"

    plt.figure()
    plt.pie(values, labels=labels, autopct=format_label, startangle=90)
    plt.title(f"Expenses for {month}")
    plt.axis('equal')

    print("\nClose the chart window to continue...")
    plt.show()