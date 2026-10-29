# Tuple-Based Course Registration Validation

## 1. Problem Statement

Develop a Python program to validate student course registrations represented as tuples. Each registration contains a student ID and a course name. The program should identify duplicate registrations, detect invalid course combinations based on predefined rules, and determine which students have violated registration requirements.

Assumptions used:

- Each registration is stored as a tuple: `(student_id, course_name)`.
- Available courses are Python, Mathematics, AI, and Web Development.
- A student cannot register for the same course more than once.
- Python and AI cannot be registered together.
- Mathematics and Web Development cannot be registered together.
- Course names must belong to the list of available courses.

## 2. Algorithm

1. Start the program.
2. Input the number of course registrations.
3. Read each student's ID and course name.
4. Store each registration as a tuple in a list.
5. Identify duplicate student-course registrations.
6. Check whether each course name is valid.
7. Group valid course selections by student.
8. Check the specified invalid course combinations.
9. Identify students who violate one or more rules.
10. Display duplicate registrations, invalid courses, rule violations, and the final summary.
11. Stop the program.

## 3. Flowchart (Mermaid TD)

\#chatgpt-mermaid-\_r_104\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_104\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_104\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_104\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_104\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_104\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_104\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_104\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_104\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_104\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_104\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_104\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_104\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_104\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_104\_ p{margin:0;}#chatgpt-mermaid-\_r_104\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_104\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_104\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_104\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_104\_ .label text,#chatgpt-mermaid-\_r_104\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_104\_ .node rect,#chatgpt-mermaid-\_r_104\_ .node circle,#chatgpt-mermaid-\_r_104\_ .node ellipse,#chatgpt-mermaid-\_r_104\_ .node polygon,#chatgpt-mermaid-\_r_104\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_104\_ .rough-node .label text,#chatgpt-mermaid-\_r_104\_ .node .label text,#chatgpt-mermaid-\_r_104\_ .image-shape .label,#chatgpt-mermaid-\_r_104\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_104\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_104\_ .rough-node .label,#chatgpt-mermaid-\_r_104\_ .node .label,#chatgpt-mermaid-\_r_104\_ .image-shape .label,#chatgpt-mermaid-\_r_104\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_104\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_104\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_104\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_104\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_104\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_104\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_104\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_104\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_104\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_104\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_104\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_104\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_104\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_104\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_104\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_104\_ .icon-shape,#chatgpt-mermaid-\_r_104\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_104\_ .icon-shape p,#chatgpt-mermaid-\_r_104\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_104\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_104\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_104\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_104\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_104\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_104\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_104\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_104\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_104\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_104\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_104\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_104\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_104\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_104\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_104\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_104\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_104\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_104\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_104\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_104\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_104\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_104\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_104\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_104\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_104\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_104\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_104\_ .node rect,#chatgpt-mermaid-\_r_104\_ .node circle,#chatgpt-mermaid-\_r_104\_ .node ellipse,#chatgpt-mermaid-\_r_104\_ .node polygon,#chatgpt-mermaid-\_r_104\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_104\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_104\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_104\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_104\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_104\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of registrationsInput student ID and courseStore registration as tupleMore registrations?Detect duplicate registrationsValidate course namesGroup courses by studentCheck invalid coursecombinationsIdentify students violatingrulesDisplay validation reportStopYesNo

## 4. Python Source Code

```
# Tuple-Based Course Registration Validationvalid_courses = {    "Python",    "Mathematics",    "AI",    "Web Development"}# Each forbidden pair is a frozensetinvalid_combinations = [    frozenset(("Python", "AI")),    frozenset(("Mathematics", "Web Development"))]registrations = []seen_registrations = set()duplicate_registrations = []invalid_courses_found = []student_courses = {}violations = {}n = int(input("Enter number of registrations: "))if n < 0:    print("Invalid number of registrations.")    raise SystemExit# Input registrations as tuplesfor i in range(n):    print(f"\nRegistration {i + 1}")    student_id = input("Enter student ID: ").strip()    course = input("Enter course name: ").strip()
```

## 5. Sample Input

```

Enter number of registrations: 7

Registration 1
Enter student ID: S101
Enter course name: Python

Registration 2
Enter student ID: S101
Enter course name: AI

Registration 3
Enter student ID: S102
Enter course name: Mathematics

Registration 4
Enter student ID: S102
Enter course name: Web Development

Registration 5
Enter student ID: S103
Enter course name: Python

Registration 6
Enter student ID: S103
Enter course name: Python

Registration 7
Enter student ID: S104
Enter course name: Biology

```

## 6. Sample Output

```

===== REGISTRATION RECORDS =====
('S101', 'Python')
('S101', 'AI')
('S102', 'Mathematics')
('S102', 'Web Development')
('S103', 'Python')
('S103', 'Python')
('S104', 'Biology')

===== DUPLICATE REGISTRATIONS =====
('S103', 'Python')

===== INVALID COURSES =====
('S104', 'Biology')

===== STUDENT VALIDATION REPORT =====

Student ID: S103
- Duplicate registration: Python

Student ID: S101
- Invalid combination: AI and Python

Student ID: S102
- Invalid combination: Mathematics and Web Development

Student ID: S104
- Invalid course: Biology

===== SUMMARY =====
Total registrations: 7
Duplicate registrations: 1
Invalid course records: 1
Students with violations: 4

```

## 7. Result

The program uses tuples to store course registrations and validates them against the specified rules. It detects duplicate registrations, invalid course names, and prohibited course combinations, then identifies students whose selections violate the registration rules.
