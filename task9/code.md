# Student Group Formation with Score Balancing – Python Project

## 1. Problem Statement

Develop a Python program to divide students into groups of specified sizes using a list of student scores. The program should allocate students so that the total scores of the groups are as balanced as possible. It must follow the given group sizes, avoid assigning a student more than once, calculate each group's total and average score, and display the difference between the highest and lowest group totals.

Allocation rules:

- Each student has a unique ID and a score.
- The group sizes are provided by the user.
- Every student must be allocated exactly once.
- Students are assigned using a greedy balancing method: process students from highest score to lowest and assign each student to the eligible group with the lowest current total score.
- If group totals are equal, choose the first eligible group.
- Group sizes must add up to the total number of students.

## 2. Algorithm

1. Start the program.
2. Input the number of students.
3. Input each student's score and store the scores in a list.
4. Input the number of groups and the required size of each group.
5. Check whether the sum of group sizes equals the number of students.
6. Sort students by score in descending order.
7. For each student, find the group with the lowest total score that has available space.
8. Assign the student to that group and update its total score.
9. Repeat until all students are allocated.
10. Display the students, group totals, average scores, and difference between the highest and lowest group totals.
11. Stop the program.

## 3. Flowchart

\#chatgpt-mermaid-\_r_15k\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_15k\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_15k\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_15k\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_15k\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_15k\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_15k\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_15k\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_15k\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_15k\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_15k\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_15k\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_15k\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_15k\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_15k\_ p{margin:0;}#chatgpt-mermaid-\_r_15k\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_15k\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_15k\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_15k\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_15k\_ .label text,#chatgpt-mermaid-\_r_15k\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_15k\_ .node rect,#chatgpt-mermaid-\_r_15k\_ .node circle,#chatgpt-mermaid-\_r_15k\_ .node ellipse,#chatgpt-mermaid-\_r_15k\_ .node polygon,#chatgpt-mermaid-\_r_15k\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_15k\_ .rough-node .label text,#chatgpt-mermaid-\_r_15k\_ .node .label text,#chatgpt-mermaid-\_r_15k\_ .image-shape .label,#chatgpt-mermaid-\_r_15k\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_15k\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_15k\_ .rough-node .label,#chatgpt-mermaid-\_r_15k\_ .node .label,#chatgpt-mermaid-\_r_15k\_ .image-shape .label,#chatgpt-mermaid-\_r_15k\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_15k\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_15k\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_15k\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_15k\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_15k\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_15k\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_15k\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_15k\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_15k\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_15k\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_15k\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_15k\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_15k\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_15k\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_15k\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_15k\_ .icon-shape,#chatgpt-mermaid-\_r_15k\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_15k\_ .icon-shape p,#chatgpt-mermaid-\_r_15k\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_15k\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_15k\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_15k\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_15k\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_15k\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_15k\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_15k\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_15k\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_15k\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15k\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_15k\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15k\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_15k\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_15k\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_15k\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_15k\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_15k\_ .node rect,#chatgpt-mermaid-\_r_15k\_ .node circle,#chatgpt-mermaid-\_r_15k\_ .node ellipse,#chatgpt-mermaid-\_r_15k\_ .node polygon,#chatgpt-mermaid-\_r_15k\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_15k\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_15k\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_15k\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_15k\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_15k\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput student scoresInput number of groups andgroup sizesDo group sizes equal studentcount?Display invalid group sizesStopSort students by scoredescendingSelect next studentFind eligible group with lowesttotalAssign student and updategroup totalAll students assigned?Calculate group averages andtotal differenceDisplay group allocation andsummaryNoYesNoYes

## 4. Python Source Code

```
# Student Group Formation with Score Balancingn = int(input("Enter number of students: "))if n <= 0:    print("Invalid number of students.")    raise SystemExitstudents = []for i in range(n):    score = float(input(f"Enter score of student {i + 1}: "))    if score < 0:        print("Scores cannot be negative.")        raise SystemExit    students.append([f"S{i + 1}", score])group_count = int(input("Enter number of groups: "))if group_count <= 0 or group_count > n:    print("Invalid number of groups.")    raise SystemExitgroup_sizes = []for i in range(group_count):    size = int(input(f"Enter size of group {i + 1}: "))    if size <= 0:        print("Group sizes must be positive.")        raise SystemExit    group_sizes.append(size)if sum(group_sizes) != n:    print("Error: Group sizes must equal the number of students.")    raise SystemExit# Sort students from highest score to loweststudents.sort(key=lambda student: student[1], reverse=True)# Each group stores student records and its current totalgroups = [[] for _ in range(group_count)]totals = [0] * group_count# Greedy score-balancing allocationfor student in students:    eligible_groups = [        i for i in range(group_count)        if len(groups[i]) < group_sizes[i]    ]    # Choose the eligible group with the lowest total    chosen = min(eligible_groups, key=lambda i: totals[i])    groups[chosen].append(student)    totals[chosen] += student[1]
```

## 5. Sample Input

```

Enter number of students: 6
Enter score of student 1: 90
Enter score of student 2: 80
Enter score of student 3: 70
Enter score of student 4: 60
Enter score of student 5: 50
Enter score of student 6: 40
Enter number of groups: 2
Enter size of group 1: 3
Enter size of group 2: 3

```

## 6. Sample Output

```

===== STUDENT GROUP ALLOCATION =====

Group 1:
S1: 90
S4: 60
S5: 50
Group Total: 200
Group Average: 66.67

Group 2:
S2: 80
S3: 70
S6: 40
Group Total: 190
Group Average: 63.33

===== SUMMARY =====
Highest Group Total: 200
Lowest Group Total: 190
Difference Between Totals: 10

```

## 7. Result

The program successfully allocates students into groups of specified sizes using a greedy score-balancing method. It calculates group totals and averages and reports the difference between the highest and lowest group totals.

Note: This greedy method aims to balance scores efficiently, but it does not guarantee the mathematically optimal allocation in every case.
