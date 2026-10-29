
# Tuple-Based Course Registration Validation

valid_courses = {
    "Python",
    "Mathematics",
    "AI",
    "Web Development"
}

# Each forbidden pair is a frozenset
invalid_combinations = [
    frozenset(("Python", "AI")),
    frozenset(("Mathematics", "Web Development"))
]

registrations = []
seen_registrations = set()
duplicate_registrations = []
invalid_courses_found = []
student_courses = {}
violations = {}

n = int(input("Enter number of registrations: "))

if n < 0:
    print("Invalid number of registrations.")
    raise SystemExit

# Input registrations as tuples
for i in range(n):
    print(f"\nRegistration {i + 1}")

    student_id = input("Enter student ID: ").strip()
    course = input("Enter course name: ").strip()

    registration = (student_id, course)
    registrations.append(registration)

    if registration in seen_registrations:
        duplicate_registrations.append(registration)
    else:
        seen_registrations.add(registration)

    # Validate required fields and course name
    if not student_id:
        violations.setdefault("<Missing ID>", []).append(
            "Missing student ID"
        )
        continue

    if not course:
        violations.setdefault(student_id, []).append(
            "Missing course name"
        )
        continue

    if course not in valid_courses:
        invalid_courses_found.append(registration)
        violations.setdefault(student_id, []).append(
            f"Invalid course: {course}"
        )
        continue

    student_courses.setdefault(student_id, []).append(course)

# Check duplicate registrations
for student_id, course in duplicate_registrations:
    if student_id:
        violations.setdefault(student_id, []).append(
            f"Duplicate registration: {course}"
        )

# Check forbidden course combinations
for student_id, courses in student_courses.items():
    selected = set(courses)

    for combination in invalid_combinations:
        if combination.issubset(selected):
            pair = " and ".join(sorted(combination))
            violations.setdefault(student_id, []).append(
                f"Invalid combination: {pair}"
            )

# Display original registrations
print("\n===== REGISTRATION RECORDS =====")
for registration in registrations:
    print(registration)

# Display duplicates
print("\n===== DUPLICATE REGISTRATIONS =====")
if duplicate_registrations:
    for registration in duplicate_registrations:
        print(registration)
else:
    print("No duplicate registrations.")

# Display invalid course names
print("\n===== INVALID COURSES =====")
if invalid_courses_found:
    for registration in invalid_courses_found:
        print(registration)
else:
    print("No invalid course names.")

# Display students who violate rules
print("\n===== STUDENT VALIDATION REPORT =====")
if violations:
    for student_id, errors in violations.items():
        print(f"\nStudent ID: {student_id}")
        for error in errors:
            print("-", error)
else:
    print("All registrations are valid.")

print("\n===== SUMMARY =====")
print("Total registrations:", len(registrations))
print("Duplicate registrations:", len(duplicate_registrations))
print("Invalid course records:", len(invalid_courses_found))
print("Students with violations:", len(violations))

