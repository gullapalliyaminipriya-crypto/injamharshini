
# University Hostel Room Allocation

students = []
rooms = []
duplicate_ids = []

n = int(input("Enter number of students: "))

if n < 0:
    print("Invalid number of students.")
    raise SystemExit

# Input student information
for i in range(n):
    print(f"\nStudent {i + 1}")
    sid = input("Enter student ID: ").strip()
    group = input("Enter group (A/B): ").strip().upper()

    if group not in ("A", "B"):
        print("Invalid group. Enter A or B.")
        raise SystemExit

    if any(s["id"] == sid for s in students):
        duplicate_ids.append(sid)
        print("Duplicate ID detected. Student not added.")
        continue

    students.append({
        "id": sid,
        "group": group
    })

# Input room information
r = int(input("\nEnter number of rooms: "))

if r < 0:
    print("Invalid number of rooms.")
    raise SystemExit

for i in range(r):
    print(f"\nRoom {i + 1}")
    room_name = input("Enter room name: ").strip()
    capacity = int(input("Enter room capacity: "))
    eligible_group = input(
        "Enter eligible group (A/B): "
    ).strip().upper()

    if capacity < 0 or eligible_group not in ("A", "B"):
        print("Invalid room capacity or group.")
        raise SystemExit

    rooms.append({
        "name": room_name,
        "capacity": capacity,
        "eligible_group": eligible_group,
        "assigned": []
    })

# Allocate students to the first eligible room with space
unallocated = []

for student in students:
    allocated = False

    for room in rooms:
        if (room["eligible_group"] == student["group"]
                and len(room["assigned"]) < room["capacity"]):
            room["assigned"].append(student["id"])
            allocated = True
            break

    if not allocated:
        unallocated.append(student["id"])

# Display allocation report
print("\n===== HOSTEL ALLOCATION REPORT =====")

for room in rooms:
    vacant = room["capacity"] - len(room["assigned"])

    print(f"\nRoom: {room['name']}")
    print(f"Eligible group: {room['eligible_group']}")
    print(f"Capacity: {room['capacity']}")
    print(f"Allocated students: {room['assigned']}")
    print(f"Students allocated: {len(room['assigned'])}")
    print(f"Vacant beds: {vacant}")

print("\n===== DUPLICATE STUDENT IDS =====")
if duplicate_ids:
    print(", ".join(duplicate_ids))
else:
    print("No duplicate IDs detected.")

print("\n===== UNALLOCATED STUDENTS =====")
if unallocated:
    print(", ".join(unallocated))
else:
    print("All valid students allocated.")

print(f"Total valid students: {len(students)}")
print(f"Total allocated: {len(students) - len(unallocated)}")
print(f"Unallocated demand: {len(unallocated)}")
print(f"Total vacant beds: {sum(room['capacity'] - len(room['assigned']) for room in rooms)}")

