roads = int(input())
intervals = int(input())

road_names = []
traffic_data = []

for i in range(roads):
    name = input()
    counts = list(map(int, input().split()))
    road_names.append(name)
    traffic_data.append(counts)

capacity = int(input())

peak_traffic = 0
peak_road = ""
peak_interval = 0

for i in range(roads):
    total = sum(traffic_data[i])
    print("Road:", road_names[i])
    print("Total vehicles:", total)

    for j in range(intervals):
        count = traffic_data[i][j]

        if count > peak_traffic:
            peak_traffic = count
            peak_road = road_names[i]
            peak_interval = j + 1

        if count > capacity:
            level = "High"
        elif count >= capacity * 0.7:
            level = "Moderate"
        else:
            level = "Low"

        print("Interval", j + 1, ":", count, "-", level)

    if max(traffic_data[i]) > capacity:
        print("Status: Exceeds capacity")
    else:
        print("Status: Within capacity")

print("Peak traffic road:", peak_road)
print("Peak traffic interval:", peak_interval)
print("Peak vehicle count:", peak_traffic)