days = int(input())

prepared = []
served = []
leftovers = []

for i in range(days):
    p, s, l = map(int, input().split())
    prepared.append(p)
    served.append(s)
    leftovers.append(l)

limit = float(input())

for i in range(days):
    if prepared[i] > 0:
        waste_percent = (leftovers[i] / prepared[i]) * 100
    else:
        waste_percent = 0

    print("Day:", i + 1)
    print("Meals Prepared:", prepared[i])
    print("Meals Served:", served[i])
    print("Leftovers:", leftovers[i])
    print("Wastage Percentage:", round(waste_percent, 2), "%")

    if waste_percent > limit:
        print("Status: Waste Limit Exceeded")
    else:
        print("Status: Acceptable")

total_prepared = sum(prepared)
total_served = sum(served)
total_leftovers = sum(leftovers)

print("Total Meals Prepared:", total_prepared)
print("Total Meals Served:", total_served)
print("Total Leftovers:", total_leftovers)

if total_prepared > 0:
    overall_waste = (total_leftovers / total_prepared) * 100
else:
    overall_waste = 0

print("Overall Wastage Percentage:", round(overall_waste, 2), "%")