n = int(input())

appliances = []
savings_list = []

for i in range(n):
    name = input()
    before, after = map(float, input().split())

    savings = before - after

    if before > 0:
        percentage = (savings / before) * 100
    else:
        percentage = 0.0

    appliances.append(name)
    savings_list.append((name, savings, percentage))

print("Energy Conservation Analysis")

for name, savings, percentage in savings_list:
    print(name)
    print("Energy Saved:", round(savings, 2))
    print("Savings Percentage:", round(percentage, 2), "%")

savings_list.sort(key=lambda x: x[1], reverse=True)

print("Appliances Ranked by Energy Savings")

for i, item in enumerate(savings_list, start=1):
    print(i, item[0], round(item[1], 2))