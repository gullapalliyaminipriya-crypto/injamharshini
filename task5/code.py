
# Integrated Student Record Consistency Checker

students = []
seen_ids = set()
duplicate_ids = set()

n = int(input("Enter number of students: "))

if n <= 0:
    print("Invalid number of students.")
    raise SystemExit

for i in range(n):
    print(f"\nStudent {i + 1}")

    sid = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    marks_input = input("Enter marks (0-100): ").strip()
    attendance_input = input(
        "Enter attendance percentage (0-100): "
    ).strip()
    courses_input = input(
        "Enter courses separated by commas: "
    ).strip()

    errors = []

    # Validate student ID
    if not sid:
        errors.append("Missing student ID")
    elif sid in seen_ids:
        duplicate_ids.add(sid)
        errors.append("Duplicate student ID")
    else:
        seen_ids.add(sid)

    # Validate student name
    if not name:
        errors.append("Missing student name")

    # Validate marks
    marks = None
    if not marks_input:
        errors.append("Missing marks")
    else:
        try:
            marks = float(marks_input)
            if not 0 <= marks <= 100:
                errors.append("Marks must be between 0 and 100")
        except ValueError:
            errors.append("Marks must be numeric")

    # Validate attendance
    attendance = None
    if not attendance_input:
        errors.append("Missing attendance")
    else:
        try:
            attendance = float(attendance_input)
            if not 0 <= attendance <= 100:
                errors.append(
                    "Attendance must be between 0 and 100"
                )
        except ValueError:
            errors.append("Attendance must be numeric")

    # Store courses as a tuple
    if not courses_input:
        courses = ()
        errors.append("Missing course records")
    else:
        courses = tuple(
            course.strip()
            for course in courses_input.split(",")
            if course.strip()
        )

        if not courses:
            errors.append("Missing course records")

        if len(courses) != len(set(courses)):
            errors.append("Duplicate course records")

    # Check required values and academic consistency
    if marks is not None and attendance is not None:
        if marks > 0 and attendance == 0:
            errors.append(
                "Marks recorded despite zero attendance"
            )

    students.append({
        "id": sid,
        "name": name,
        "marks": marks,
        "attendance": attendance,
        "courses": courses,
        "errors": errors
    })

# Report all records
print("\n===== STUDENT RECORD VALIDATION =====")

valid_count = 0
invalid_count = 0

for student in students:
    print(f"\nStudent ID: {student['id'] or 'Missing'}")
    print(f"Name: {student['name'] or 'Missing'}")
    print(f"Marks: {student['marks']}")
    print(f"Attendance: {student['attendance']}")
    print(f"Courses: {student['courses']}")

    if student["errors"]:
        invalid_count += 1
        print("Status: INCONSISTENT")
        for error in student["errors"]:
            print("-", error)
    else:
        valid_count += 1
        print("Status: VALID")

# Final summary
print("\n===== CONSISTENCY SUMMARY =====")
print("Total records:", len(students))
print("Valid records:", valid_count)
print("Inconsistent records:", invalid_count)
print("Duplicate student IDs:", len(duplicate_ids))

if duplicate_ids:
    print("Duplicate IDs found:", ", ".join(sorted(duplicate_ids)))
else:
    print("No duplicate student IDs found.")

