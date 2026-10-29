
# Energy Conservation Before-and-After Analysis

appliances = []

n = int(input("Enter number of appliances: "))

if n <= 0:
    print("Invalid number of appliances.")
    raise SystemExit

for i in range(n):
    print(f"\nAppliance {i + 1}")

    name = input("Enter appliance name: ").strip()
    before = float(input("Enter usage before intervention (kWh): "))
    after = float(input("Enter usage after intervention (kWh): "))

    if not name or before < 0 or after < 0:
        print("Invalid name or usage value.")
        raise SystemExit

    savings = before - after

    if before > 0:
        percentage = (savings / before) * 100
    else:
        percentage = None

    if savings > 0:
        status = "Energy saved"
    elif savings < 0:
        status = "Consumption increased"
    else:
        status = "No change"

    appliances.append({
        "name": name,
        "before": before,
        "after": after,
        "savings": savings,
        "percentage": percentage,
        "status": status
    })

# Calculate overall totals
total_before = sum(a["before"] for a in appliances)
total_after = sum(a["after"] for a in appliances)
total_savings = total_before - total_after

if total_before > 0:
    overall_percentage = total_savings / total_before * 100
else:
    overall_percentage = None

# Display appliance-wise analysis
print("\n===== ENERGY CONSERVATION REPORT =====")

for a in appliances:
    print(f"\nAppliance: {a['name']}")
    print(f"Before usage: {a['before']:.2f} kWh")
    print(f"After usage: {a['after']:.2f} kWh")
    print(f"Energy savings: {a['savings']:.2f} kWh")

    if a["percentage"] is not None:
        print(f"Savings percentage: {a['percentage']:.2f}%")
    else:
        print("Savings percentage: Undefined (zero initial usage)")

    print(f"Status: {a['status']}")

# Rank by savings, highest first
ranked = sorted(
    appliances,
    key=lambda a: a["savings"],
    reverse=True
)

print("\n===== APPLIANCE SAVINGS RANKING =====")

for rank, a in enumerate(ranked, start=1):
    print(
        f"{rank}. {a['name']} - "
        f"{a['savings']:.2f} kWh saved"
    )

# Display overall results
print("\n===== OVERALL SUMMARY =====")
print(f"Total before usage: {total_before:.2f} kWh")
print(f"Total after usage: {total_after:.2f} kWh")
print(f"Total energy savings: {total_savings:.2f} kWh")

if overall_percentage is not None:
    print(f"Overall savings percentage: {overall_percentage:.2f}%")
else:
    print("Overall savings percentage: Undefined")

if total_savings > 0:
    print("Overall result: Energy consumption reduced")
elif total_savings < 0:
    print("Overall result: Energy consumption increased")
else:
    print("Overall result: No overall change")

