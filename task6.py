areas = int(input())
days = int(input())

area_names = []
total_demand = []
total_supply = []

for i in range(areas):
    name = input()
    area_names.append(name)

    demand_sum = 0
    supply_sum = 0

    for j in range(days):
        demand, supply = map(float, input().split())
        demand_sum += demand
        supply_sum += supply

    total_demand.append(demand_sum)
    total_supply.append(supply_sum)

print("Area-wise Water Distribution Analysis")

for i in range(areas):
    shortage = max(0, total_demand[i] - total_supply[i])

    if total_demand[i] > 0:
        percentage = (total_supply[i] / total_demand[i]) * 100
    else:
        percentage = 100

    print(area_names[i])
    print("Total Demand:", round(total_demand[i], 2))
    print("Total Supply:", round(total_supply[i], 2))
    print("Shortage:", round(shortage, 2))
    print("Supply Percentage:", round(percentage, 2), "%")

most_underserved = -1
worst_area = ""

for i in range(areas):
    shortage = total_demand[i] - total_supply[i]

    if shortage > most_underserved:
        most_underserved = shortage
        worst_area = area_names[i]

print("Most Underserved Area:", worst_area)