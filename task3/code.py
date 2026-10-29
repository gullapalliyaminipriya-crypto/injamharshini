
# Multi-Branch Retail Inventory Transfer

branches = []
products = []

n = int(input("Enter number of branches: "))
p = int(input("Enter number of products: "))
max_transfer = int(input("Enter maximum quantity per transfer: "))

if n <= 0 or p <= 0 or max_transfer <= 0:
    print("Invalid input.")
    raise SystemExit

# Input product names
for i in range(p):
    product = input(f"Enter product {i + 1} name: ")
    products.append(product)

# Input branch stock and target levels
for i in range(n):
    name = input(f"\nEnter branch {i + 1} name: ")
    stock = []
    target = []

    for product in products:
        current = int(input(f"{product} current stock: "))
        required = int(input(f"{product} target stock: "))

        if current < 0 or required < 0:
            print("Stock and target values cannot be negative.")
            raise SystemExit

        stock.append(current)
        target.append(required)

    branches.append({
        "name": name,
        "stock": stock,
        "target": target
    })

# Calculate initial surplus and shortage
surplus = []
shortage = []

for branch in branches:
    surplus.append([
        max(0, branch["stock"][j] - branch["target"][j])
        for j in range(p)
    ])
    shortage.append([
        max(0, branch["target"][j] - branch["stock"][j])
        for j in range(p)
    ])

# Generate transfers, respecting the transfer limit
transfers = []

for j in range(p):
    for donor in range(n):
        for recipient in range(n):
            if donor == recipient:
                continue

            while surplus[donor][j] > 0 and shortage[recipient][j] > 0:
                quantity = min(
                    surplus[donor][j],
                    shortage[recipient][j],
                    max_transfer
                )

                if quantity <= 0:
                    break

                surplus[donor][j] -= quantity
                shortage[recipient][j] -= quantity

                branches[donor]["stock"][j] -= quantity
                branches[recipient]["stock"][j] += quantity

                transfers.append({
                    "product": products[j],
                    "from": branches[donor]["name"],
                    "to": branches[recipient]["name"],
                    "quantity": quantity
                })

# Display initial surplus and shortage
print("\n===== INITIAL INVENTORY ANALYSIS =====")

for i, branch in enumerate(branches):
    print(f"\nBranch: {branch['name']}")

    for j, product in enumerate(products):
        print(
            f"{product}: Surplus = "
            f"{max(0, branch['stock'][j] - branch['target'][j])}, "
            f"Shortage = "
            f"{max(0, branch['target'][j] - branch['stock'][j])}"
        )

# Display transfer plan
print("\n===== TRANSFER PLAN =====")

if transfers:
    for t in transfers:
        print(
            f"{t['product']}: {t['quantity']} units "
            f"from {t['from']} to {t['to']}"
        )
else:
    print("No transfers required.")

# Display final stock and remaining shortages
print("\n===== FINAL INVENTORY =====")

total_shortage = 0

for i, branch in enumerate(branches):
    print(f"\nBranch: {branch['name']}")

    for j, product in enumerate(products):
        final_stock = branch["stock"][j]
        target_stock = branch["target"][j]
        remaining = max(0, target_stock - final_stock)
        total_shortage += remaining

        print(
            f"{product}: Final stock = {final_stock}, "
            f"Target = {target_stock}, "
            f"Remaining shortage = {remaining}"
        )

print("\nTotal transfer transactions:", len(transfers))
print("Total units transferred:", sum(t["quantity"] for t in transfers))
print("Total remaining shortage:", total_shortage)

