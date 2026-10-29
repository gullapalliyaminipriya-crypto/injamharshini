# University Hostel Room Allocation

## 1. Problem Statement

Develop a Python program to allocate students to university hostel rooms based on room capacity, student eligibility, and grouping constraints. The program should check whether students meet the eligibility requirements for each room, prevent room capacity from being exceeded, detect duplicate student assignments, and calculate the number of students who remain unallocated.

Assumptions used:

- Each student has a unique student ID and a group (A or B).
- Each room has a fixed capacity and an eligible group.
- Students can be assigned only to rooms matching their group.
- A student must not be assigned to more than one room.
- Students are allocated in input order until eligible rooms have no remaining capacity.

## 2. Algorithm

1. Start the program.
2. Input the number of students and their IDs and groups.
3. Input the number of rooms, their capacities, and eligible groups.
4. Check for duplicate student IDs.
5. Allocate each student to the first eligible room with available capacity.
6. Prevent duplicate assignments and reject ineligible allocations.
7. Record students who cannot be allocated.
8. Calculate the remaining capacity of each room and total unallocated demand.
9. Display room-wise assignments, duplicate records, and unallocated students.
10. Stop the program.

## 3. Flowchart (Mermaid TD)

\#chatgpt-mermaid-\_r_m5\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_m5\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_m5\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_m5\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_m5\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_m5\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_m5\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_m5\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_m5\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_m5\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_m5\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_m5\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_m5\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_m5\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_m5\_ p{margin:0;}#chatgpt-mermaid-\_r_m5\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_m5\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_m5\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_m5\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_m5\_ .label text,#chatgpt-mermaid-\_r_m5\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_m5\_ .node rect,#chatgpt-mermaid-\_r_m5\_ .node circle,#chatgpt-mermaid-\_r_m5\_ .node ellipse,#chatgpt-mermaid-\_r_m5\_ .node polygon,#chatgpt-mermaid-\_r_m5\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_m5\_ .rough-node .label text,#chatgpt-mermaid-\_r_m5\_ .node .label text,#chatgpt-mermaid-\_r_m5\_ .image-shape .label,#chatgpt-mermaid-\_r_m5\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_m5\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_m5\_ .rough-node .label,#chatgpt-mermaid-\_r_m5\_ .node .label,#chatgpt-mermaid-\_r_m5\_ .image-shape .label,#chatgpt-mermaid-\_r_m5\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_m5\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_m5\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_m5\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_m5\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_m5\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_m5\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_m5\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_m5\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_m5\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_m5\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_m5\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_m5\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_m5\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_m5\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_m5\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_m5\_ .icon-shape,#chatgpt-mermaid-\_r_m5\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_m5\_ .icon-shape p,#chatgpt-mermaid-\_r_m5\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_m5\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_m5\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_m5\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_m5\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_m5\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_m5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_m5\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_m5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_m5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_m5\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_m5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_m5\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_m5\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_m5\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_m5\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_m5\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_m5\_ .node rect,#chatgpt-mermaid-\_r_m5\_ .node circle,#chatgpt-mermaid-\_r_m5\_ .node ellipse,#chatgpt-mermaid-\_r_m5\_ .node polygon,#chatgpt-mermaid-\_r_m5\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_m5\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_m5\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_m5\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_m5\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_m5\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput student detailsInput room capacity andeligibilityCheck duplicate student IDsSelect next studentEligible room available?Allocate student to roomAdd student to unallocated listMore students?Calculate vacant capacity andunallocated demandDisplay allocation reportStopYesNoYesNo

## 4. Python Source Code

```
# University Hostel Room Allocationstudents = []rooms = []duplicate_ids = []n = int(input("Enter number of students: "))if n < 0:    print("Invalid number of students.")    raise SystemExit# Input student informationfor i in range(n):    print(f"\nStudent {i + 1}")    sid = input("Enter student ID: ").strip()    group = input("Enter group (A/B): ").strip().upper()    if group not in ("A", "B"):        print("Invalid group. Enter A or B.")        raise SystemExit    if any(s["id"] == sid for s in students):        duplicate_ids.append(sid)        print("Duplicate ID detected. Student not added.")        continue    students.append({        "id": sid,        "group": group    })# Input room informationr = int(input("\nEnter number of rooms: "))
```

## 5. Sample Input

```

Enter number of students: 5

Student 1
Enter student ID: S101
Enter group (A/B): A

Student 2
Enter student ID: S102
Enter group (A/B): B

Student 3
Enter student ID: S103
Enter group (A/B): A

Student 4
Enter student ID: S102
Enter group (A/B): B
Duplicate ID detected. Student not added.

Student 5
Enter student ID: S104
Enter group (A/B): B

Enter number of rooms: 2

Room 1
Enter room name: Room-A
Enter room capacity: 2
Enter eligible group (A/B): A

Room 2
Enter room name: Room-B
Enter room capacity: 1
Enter eligible group (A/B): B

```

## 6. Sample Output

```

===== HOSTEL ALLOCATION REPORT =====

Room: Room-A
Eligible group: A
Capacity: 2
Allocated students: ['S101', 'S103']
Students allocated: 2
Vacant beds: 0

Room: Room-B
Eligible group: B
Capacity: 1
Allocated students: ['S102']
Students allocated: 1
Vacant beds: 0

===== DUPLICATE STUDENT IDS =====
S102

===== UNALLOCATED STUDENTS =====
S104
Total valid students: 4
Total allocated: 3
Unallocated demand: 1
Total vacant beds: 0

```

## 7. Result

The program allocates students according to room capacity and group eligibility, detects duplicate student IDs, and identifies students who could not be accommodated. In this example, three students are allocated, one student remains unallocated, and one duplicate ID is detected.
