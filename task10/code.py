
# Smart Public Transport Fare Reconciliation

STUDENT_DISCOUNT = 0.25
SENIOR_DISCOUNT = 0.40

routes = []

n = int(input("Enter number of routes: "))

if n <= 0:
    print("Invalid number of routes.")
    raise SystemExit

for i in range(n):
    print(f"\nRoute {i + 1}")

    route_name = input("Enter route name: ")
    base_fare = float(input("Enter base fare: Rs. "))

    if base_fare < 0:
        print("Fare cannot be negative.")
        raise SystemExit

    adults = int(input("Enter adult tickets sold: "))
    students = int(input("Enter student tickets sold: "))
    seniors = int(input("Enter senior citizen tickets sold: "))

    if adults < 0 or students < 0 or seniors < 0:
        print("Ticket quantities cannot be negative.")
        raise SystemExit

    collected = float(
        input("Enter actual collected revenue: Rs. ")
    )

    if collected < 0:
        print("Revenue cannot be negative.")
        raise SystemExit

    # Calculate discounted fares
    adult_fare = base_fare
    student_fare = base_fare * (1 - STUDENT_DISCOUNT)
    senior_fare = base_fare * (1 - SENIOR_DISCOUNT)

    # Calculate expected revenue
    adult_revenue = adults * adult_fare
    student_revenue = students * student_fare
    senior_revenue = seniors * senior_fare

    expected = (
        adult_revenue + student_revenue + senior_revenue
    )

    # Reconcile revenue
    discrepancy = collected - expected

    if discrepancy > 0:
        status = "Excess collection"
    elif discrepancy < 0:
        status = "Revenue shortage"
    else:
        status = "Exact match"

    routes.append({
        "name": route_name,
        "adults": adults,
        "students": students,
        "seniors": seniors,
        "expected": expected,
        "collected": collected,
        "discrepancy": discrepancy,
        "status": status
    })

# Display route-wise report
print("\n===== FARE RECONCILIATION REPORT =====")

for route in routes:
    print(f"\nRoute: {route['name']}")
    print(f"Adult tickets: {route['adults']}")
    print(f"Student tickets: {route['students']}")
    print(f"Senior citizen tickets: {route['seniors']}")
    print(f"Expected revenue: Rs. {route['expected']:.2f}")
    print(f"Collected revenue: Rs. {route['collected']:.2f}")
    print(f"Discrepancy: Rs. {route['discrepancy']:.2f}")
    print(f"Status: {route['status']}")

# Calculate overall totals
total_expected = sum(r["expected"] for r in routes)
total_collected = sum(r["collected"] for r in routes)
total_discrepancy = total_collected - total_expected

print("\n===== OVERALL SUMMARY =====")
print(f"Total expected revenue: Rs. {total_expected:.2f}")
print(f"Total collected revenue: Rs. {total_collected:.2f}")
print(f"Overall discrepancy: Rs. {total_discrepancy:.2f}")

if total_discrepancy > 0:
    print("Overall status: Excess collection")
elif total_discrepancy < 0:
    print("Overall status: Revenue shortage")
else:
    print("Overall status: Revenue reconciled exactly")

