
# Student Group Formation with Score Balancing

n = int(input("Enter number of students: "))

if n <= 0:
    print("Invalid number of students.")
    raise SystemExit

students = []

for i in range(n):
    score = float(input(f"Enter score of student {i + 1}: "))

    if score < 0:
        print("Scores cannot be negative.")
        raise SystemExit

    students.append([f"S{i + 1}", score])

group_count = int(input("Enter number of groups: "))

if group_count <= 0 or group_count > n:
    print("Invalid number of groups.")
    raise SystemExit

group_sizes = []

for i in range(group_count):
    size = int(input(f"Enter size of group {i + 1}: "))

    if size <= 0:
        print("Group sizes must be positive.")
        raise SystemExit

    group_sizes.append(size)

if sum(group_sizes) != n:
    print("Error: Group sizes must equal the number of students.")
    raise SystemExit

# Sort students from highest score to lowest
students.sort(key=lambda student: student[1], reverse=True)

# Each group stores student records and its current total
groups = [[] for _ in range(group_count)]
totals = [0] * group_count

# Greedy score-balancing allocation
for student in students:
    eligible_groups = [
        i for i in range(group_count)
        if len(groups[i]) < group_sizes[i]
    ]

    # Choose the eligible group with the lowest total
    chosen = min(eligible_groups, key=lambda i: totals[i])

    groups[chosen].append(student)
    totals[chosen] += student[1]

# Display group details
print("\n===== STUDENT GROUP ALLOCATION =====")

for i in range(group_count):
    print(f"\nGroup {i + 1}:")

    for student_id, score in groups[i]:
        print(f"{student_id}: {score:g}")

    average = totals[i] / len(groups[i])
    print(f"Group Total: {totals[i]:g}")
    print(f"Group Average: {average:.2f}")

# Calculate difference between highest and lowest totals
difference = max(totals) - min(totals)

print("\n===== SUMMARY =====")
print(f"Highest Group Total: {max(totals):g}")
print(f"Lowest Group Total: {min(totals):g}")
print(f"Difference Between Totals: {difference:g}")

