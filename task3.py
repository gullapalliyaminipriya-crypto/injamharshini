wards = int(input())
days = int(input())

ward_names = []
occupancy = []

for i in range(wards):
    name = input()
    counts = list(map(int, input().split()))
    ward_names.append(name)
    occupancy.append(counts)

capacities = list(map(int, input().split()))

peak_count = -1
peak_ward = ""
peak_day = 0

for i in range(wards):
    print("Ward:", ward_names[i])

    for j in range(days):
        count = occupancy[i][j]
        capacity = capacities[i]

        utilization = (count / capacity) * 100

        print("Day", j + 1)
        print("Occupied beds:", count)
        print("Utilization:", round(utilization, 2), "%")

        if count > capacity:
            print("Status: Capacity Exceeded")
        else:
            print("Status: Within Capacity")

        if count > peak_count:
            peak_count = count
            peak_ward = ward_names[i]
            peak_day = j + 1

print("Peak Demand Ward:", peak_ward)
print("Peak Demand Day:", peak_day)
print("Peak Occupancy:", peak_count)