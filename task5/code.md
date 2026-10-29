# Integrated Student Record Consistency Checker

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

\#chatgpt-mermaid-\_r_s6\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_s6\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_s6\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_s6\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_s6\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_s6\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_s6\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_s6\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_s6\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_s6\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_s6\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_s6\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_s6\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_s6\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_s6\_ p{margin:0;}#chatgpt-mermaid-\_r_s6\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_s6\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_s6\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_s6\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_s6\_ .label text,#chatgpt-mermaid-\_r_s6\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_s6\_ .node rect,#chatgpt-mermaid-\_r_s6\_ .node circle,#chatgpt-mermaid-\_r_s6\_ .node ellipse,#chatgpt-mermaid-\_r_s6\_ .node polygon,#chatgpt-mermaid-\_r_s6\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_s6\_ .rough-node .label text,#chatgpt-mermaid-\_r_s6\_ .node .label text,#chatgpt-mermaid-\_r_s6\_ .image-shape .label,#chatgpt-mermaid-\_r_s6\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_s6\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_s6\_ .rough-node .label,#chatgpt-mermaid-\_r_s6\_ .node .label,#chatgpt-mermaid-\_r_s6\_ .image-shape .label,#chatgpt-mermaid-\_r_s6\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_s6\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_s6\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_s6\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_s6\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_s6\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_s6\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_s6\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_s6\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_s6\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_s6\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_s6\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_s6\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_s6\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_s6\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_s6\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_s6\_ .icon-shape,#chatgpt-mermaid-\_r_s6\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_s6\_ .icon-shape p,#chatgpt-mermaid-\_r_s6\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_s6\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_s6\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_s6\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_s6\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_s6\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_s6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_s6\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_s6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_s6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_s6\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_s6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_s6\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_s6\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_s6\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_s6\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_s6\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_s6\_ .node rect,#chatgpt-mermaid-\_r_s6\_ .node circle,#chatgpt-mermaid-\_r_s6\_ .node ellipse,#chatgpt-mermaid-\_r_s6\_ .node polygon,#chatgpt-mermaid-\_r_s6\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_s6\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_s6\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_s6\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_s6\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_s6\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of studentsInput student details andcoursesStore records in lists and tuplesValidate ID and nameCheck duplicate IDs andmissing valuesValidate marks and attendanceValidate course recordsMore student records?Display valid records and errorsCalculate consistency summaryStopYesNo

## 4. Python Source Code

```
# Integrated Student Record Consistency Checkerstudents = []seen_ids = set()duplicate_ids = set()n = int(input("Enter number of students: "))if n <= 0:    print("Invalid number of students.")    raise SystemExitfor i in range(n):    print(f"\nStudent {i + 1}")    sid = input("Enter student ID: ").strip()    name = input("Enter student name: ").strip()    marks_input = input("Enter marks (0-100): ").strip()    attendance_input = input(        "Enter attendance percentage (0-100): "    ).strip()    courses_input = input(        "Enter courses separated by commas: "    ).strip()    errors = []    # Validate student ID    if not sid:        errors.append("Missing student ID")    elif sid in seen_ids:        duplicate_ids.add(sid)        errors.append("Duplicate student ID")    else:        seen_ids.add(sid)
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

## 7. Result

The program successfully validates student identifiers, names, marks, attendance, and course records using Python lists and tuples. It detects duplicate IDs, missing values, invalid academic data, and inconsistent records, then generates a summary of valid and inconsistent student records.
