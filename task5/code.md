

## 1. Problem Statement

Develop a Python program to validate student academic records stored using lists and tuples. The program should check student identifiers, names, marks, attendance percentages, and course records. It must detect duplicate student IDs, missing values, invalid marks, invalid attendance, and inconsistent course information. Finally, the program should display valid records, list errors, and calculate the number of inconsistent records.

Assumptions used:

- Student IDs must be unique.
- Student names cannot be empty.
- Marks must be between 0 and 100.
- Attendance must be between 0% and 100%.
- Each student must have at least one valid course.
- Missing or invalid values are reported as errors.

## 2. Algorithm

1. Start the program.
2. Input the number of student records.
3. Read each student's ID, name, marks, attendance, and course details.
4. Store student records in lists and course records in tuples.
5. Check for duplicate student IDs.
6. Validate names and identify missing values.
7. Check that marks and attendance are within valid ranges.
8. Validate course records and identify missing or duplicate courses.
9. Store validation errors for each student.
10. Display student records, detected errors, and the final consistency summary.
11. Stop the program.

## 3. Flowchart (Mermaid TD)
```mermaid
flowchart TD
    A([START]) --> B[/Enter Number/]
    B --> C{Number is Even?}
    C -->|YES| D[Print Even]
    C -->|NO| E[Print Odd]
    D --> F([STOP])
    E --> F
```


## 5. Sample Input

```

Enter number of students: 3

Student 1
Enter student ID: S101
Enter student name: Ravi
Enter marks (0-100): 85
Enter attendance percentage (0-100): 90
Enter courses separated by commas: Python,Math

Student 2
Enter student ID: S101
Enter student name: Priya
Enter marks (0-100): 75
Enter attendance percentage (0-100): 80
Enter courses separated by commas: Python

Student 3
Enter student ID: S103
Enter student name:
Enter marks (0-100): 105
Enter attendance percentage (0-100): 0
Enter courses separated by commas:

```

## 6. Sample Output

```

===== STUDENT RECORD VALIDATION =====

Student ID: S101
Name: Ravi
Marks: 85.0
Attendance: 90.0
Courses: ('Python', 'Math')
Status: VALID

Student ID: S101
Name: Priya
Marks: 75.0
Attendance: 80.0
Courses: ('Python',)
Status: INCONSISTENT
- Duplicate student ID

Student ID: S103
Name: Missing
Marks: 105.0
Attendance: 0.0
Courses: ()
Status: INCONSISTENT
- Missing student name
- Marks must be between 0 and 100
- Missing course records
- Marks recorded despite zero attendance

===== CONSISTENCY SUMMARY =====
Total records: 3
Valid records: 1
Inconsistent records: 2
Duplicate student IDs: 1
Duplicate IDs found: S101

```
