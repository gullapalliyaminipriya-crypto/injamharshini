
# Integrated Warehouse Order Prioritization

stock = {}

# Input product stock
n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products.")
    raise SystemExit

for i in range(n):
    name = input("Enter product name: ").strip()
    quantity = int(input("Enter available stock: "))

    if quantity < 0:
        print("Stock cannot be negative.")
        raise SystemExit

    if name in stock:
        print("Duplicate product name.")
        raise SystemExit

    stock[name] = quantity

# Input customer orders
m = int(input("\nEnter number of orders: "))

if m < 0:
    print("Invalid number of orders.")
    raise SystemExit

orders = []
priority_order = {"High": 1, "Medium": 2, "Low": 3}

for i in range(m):
    print(f"\nOrder {i + 1}")
    order_id = input("Enter order ID: ").strip()
    product = input("Enter product name: ").strip()
    quantity = int(input("Enter order quantity: "))
    priority = input(
        "Enter priority (High/Medium/Low): "
    ).strip().capitalize()

    if quantity <= 0 or priority not in priority_order:
        print("Invalid quantity or priority.")
        raise SystemExit

    orders.append({
        "id": order_id,
        "product": product,
        "quantity": quantity,
        "priority": priority,
        "input_order": i
    })

# Sort by priority; retain input order for ties
orders.sort(key=lambda o: priority_order[o["priority"]])

# Process orders
report = []

for order in orders:
    product = order["product"]
    requested = order["quantity"]

    if product not in stock:
        fulfilled = 0
        status = "Product unavailable"
    else:
        fulfilled = min(requested, stock[product])
        stock[product] -= fulfilled

        if fulfilled == requested:
            status = "Fully fulfilled"
        elif fulfilled > 0:
            status = "Partially fulfilled"
        else:
            status = "Unfulfilled"

    outstanding = requested - fulfilled

    report.append({
        **order,
        "fulfilled": fulfilled,
        "outstanding": outstanding,
        "status": status
    })

# Display fulfilment report
print("\n===== ORDER FULFILMENT REPORT =====")

for order in report:
    print(f"\nOrder ID: {order['id']}")
    print(f"Product: {order['product']}")
    print(f"Priority: {order['priority']}")
    print(f"Ordered quantity: {order['quantity']}")
    print(f"Fulfilled quantity: {order['fulfilled']}")
    print(f"Outstanding quantity: {order['outstanding']}")
    print(f"Status: {order['status']}")

# Display remaining stock
print("\n===== REMAINING WAREHOUSE STOCK =====")

for product, quantity in stock.items():
    print(f"{product}: {quantity} units")

total_ordered = sum(o["quantity"] for o in report)
total_fulfilled = sum(o["fulfilled"] for o in report)
total_outstanding = sum(o["outstanding"] for o in report)

print("\n===== SUMMARY =====")
print("Total quantity ordered:", total_ordered)
print("Total quantity fulfilled:", total_fulfilled)
print("Total outstanding quantity:", total_outstanding)

