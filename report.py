def monthly_report(data, month):
    total = 0
    category_data = {}

    for item in data:
        date = item["date"].strip()
        category = item["category"].strip()

        # Skip invalid rows
        if not date or not category:
            continue

        # Ensure correct month match
        if not date.startswith(month):
            continue

        try:
            amount = float(item["amount"].strip())
        except ValueError:
            continue

        total += amount

        if category not in category_data:
            category_data[category] = 0

        category_data[category] += amount

    if not category_data:
        return None

    top_category = max(category_data, key=category_data.get)

    return total, category_data, top_category