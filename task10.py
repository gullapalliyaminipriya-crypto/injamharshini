n = int(input())

areas = []

for i in range(n):
    name, required, available, urgency = input().split()
    areas.append([name, int(required), int(available), int(urgency)])

stock = int(input())

# Prioritize areas with higher urgency
areas.sort(key=lambda x: x[3], reverse=True)

print("Disaster Relief Supply Allocation")

for area in areas:
    name, required, available, urgency = area

    shortage = max(0, required - available)
    allocation = min(shortage, stock)

    stock -= allocation
    unmet = shortage - allocation

    print("Area:", name)
    print("Shortage:", shortage)
    print("Additional Supply Allocated:", allocation)
    print("Unmet Demand:", unmet)

print("Remaining Relief Stock:", stock)