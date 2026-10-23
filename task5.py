n = int(input())

items = []
prices = []
stock = []

for i in range(n):
    name, price, quantity = input().split()
    items.append(name)
    prices.append(float(price))
    stock.append(int(quantity))

orders = int(input())
total_sales = 0

for i in range(orders):
    name, quantity = input().split()
    quantity = int(quantity)

    if name not in items:
        print("Item not available")
        continue

    index = items.index(name)

    if quantity <= 0:
        print("Invalid quantity")
    elif quantity > stock[index]:
        print("Insufficient stock")
    else:
        bill = quantity * prices[index]
        stock[index] -= quantity
        total_sales += bill

        print("Item:", name)
        print("Quantity:", quantity)
        print("Bill: Rs.", round(bill, 2))
        print("Order successful")

print("Total Daily Sales: Rs.", round(total_sales, 2))
print("Remaining Stock:")

for i in range(n):
    print(items[i], stock[i])