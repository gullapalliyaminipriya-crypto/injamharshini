
# Integrated Campus Energy and Water Audit

ELECTRICITY_RATE = 8
WATER_RATE = 30
ELECTRICITY_LIMIT = 100
WATER_LIMIT = 10

buildings = []
n = int(input("Enter number of buildings: "))
days = int(input("Enter number of days: "))

if n <= 0 or days <= 0:
    print("Invalid number of buildings or days.")
    raise SystemExit

for i in range(n):
    name = input("\nEnter building name: ")
    electricity = []
    water = []

    for d in range(days):
        e = float(input(
            f"Day {d + 1} electricity (kWh): "
        ))
        w = float(input(
            f"Day {d + 1} water (kL): "
        ))

        if e < 0 or w < 0:
            print("Consumption cannot be negative.")
            raise SystemExit

        electricity.append(e)
        water.append(w)

    total_e = sum(electricity)
    total_w = sum(water)

    avg_e = total_e / days
    avg_w = total_w / days

    electricity_cost = total_e * ELECTRICITY_RATE
    water_cost = total_w * WATER_RATE
    total_cost = electricity_cost + water_cost

    if electricity[0] != 0:
        e_change = (
            (electricity[-1] - electricity[0])
            / electricity[0]
        ) * 100
    else:
        e_change = 0 if electricity[-1] == 0 else None

    if water[0] != 0:
        w_change = (
            (water[-1] - water[0]) / water[0]
        ) * 100
    else:
        w_change = 0 if water[-1] == 0 else None

    excessive = []
    if avg_e > ELECTRICITY_LIMIT:
        excessive.append("Electricity")
    if avg_w > WATER_LIMIT:
        excessive.append("Water")

    # Lower consumption gives a lower score.
    # Score = 60% electricity + 40% water.
    score = (0.6 * avg_e / ELECTRICITY_LIMIT
             + 0.4 * avg_w / WATER_LIMIT) * 100

    buildings.append({
        "name": name,
        "total_e": total_e,
        "total_w": total_w,
        "avg_e": avg_e,
        "avg_w": avg_w,
        "electricity_cost": electricity_cost,
        "water_cost": water_cost,
        "total_cost": total_cost,
        "e_change": e_change,
        "w_change": w_change,
        "excessive": excessive,
        "score": score
    })

# Display individual building reports
print("\n========== CAMPUS AUDIT REPORT ==========")

for b in buildings:
    print(f"\nBuilding: {b['name']}")
    print(f"Total electricity: {b['total_e']:.2f} kWh")
    print(f"Total water: {b['total_w']:.2f} kL")
    print(f"Average electricity: {b['avg_e']:.2f} kWh/day")
    print(f"Average water: {b['avg_w']:.2f} kL/day")
    print(f"Electricity cost: Rs. {b['electricity_cost']:.2f}")
    print(f"Water cost: Rs. {b['water_cost']:.2f}")
    print(f"Total cost: Rs. {b['total_cost']:.2f}")

    e_text = (
        f"{b['e_change']:.2f}%"
        if b["e_change"] is not None
        else "Undefined (first day is zero)"
    )
    w_text = (
        f"{b['w_change']:.2f}%"
        if b["w_change"] is not None
        else "Undefined (first day is zero)"
    )

    print(f"Electricity percentage change: {e_text}")
    print(f"Water percentage change: {w_text}")

    if b["excessive"]:
        print("Warning: Excessive " + ", ".join(b["excessive"]))
    else:
        print("Consumption status: Normal")

    print(f"Combined score: {b['score']:.2f}")

# Lowest score ranks first
ranked = sorted(buildings, key=lambda b: b["score"])

print("\n========== BUILDING RANKING ==========")
for rank, b in enumerate(ranked, start=1):
    print(f"{rank}. {b['name']} - Score: {b['score']:.2f}")

print("\n========== CAMPUS TOTALS ==========")
print(f"Total electricity: {sum(b['total_e'] for b in buildings):.2f} kWh")
print(f"Total water: {sum(b['total_w'] for b in buildings):.2f} kL")
print(f"Total expenditure: Rs. {sum(b['total_cost'] for b in buildings):.2f}")

