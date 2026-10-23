n = int(input())

locations = []

for i in range(n):
    name = input()
    received, distributed, damaged, remaining = map(int, input().split())

    expected = received - distributed - damaged
    discrepancy = remaining - expected

    replenishment = max(0, 100 - remaining)

    locations.append(
        (name, received, distributed, damaged,
         remaining, discrepancy, replenishment)
    )

print("Food Supply Chain Stock Reconciliation")

for item in locations:
    name, received, distributed, damaged, remaining, discrepancy, replenishment = item

    print("Location:", name)
    print("Expected Stock:", received - distributed - damaged)
    print("Actual Remaining Stock:", remaining)

    if discrepancy == 0:
        print("Status: Stock Matched")
    else:
        print("Discrepancy:", discrepancy)

    print("Replenishment Required:", replenishment)

print("Locations with Discrepancies:")

found = False
for item in locations:
    if item[5] != 0:
        print(item[0])
        found = True

if not found:
    print("None")