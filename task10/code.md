# Smart Public Transport Fare Reconciliation

## 1. Problem Statement

Develop a Python program to calculate passenger fares across multiple public transport routes and passenger categories. The program should apply route-based fares, passenger-category concessions, and ticket quantities to calculate the expected revenue. It should then compare expected revenue with the actual collected revenue, identify discrepancies, and generate a reconciliation report for each route.

Assumptions used:

- Adult passengers pay the full route fare.
- Student passengers receive a 25% discount.
- Senior citizens receive a 40% discount.
- Expected revenue is calculated using the discounted fares and number of tickets sold.
- Discrepancy = Collected revenue − Expected revenue.
- A positive discrepancy indicates excess collection; a negative discrepancy indicates a shortage.

## 2. Algorithm

1. Start the program.
2. Input the number of transport routes.
3. For each route, input the route name and base fare.
4. Input the number of adult, student, and senior citizen tickets sold.
5. Calculate the fare for each passenger category after applying discounts.
6. Calculate expected revenue for the route.
7. Input the actual collected revenue.
8. Calculate the discrepancy between collected and expected revenue.
9. Classify the discrepancy as excess collection, revenue shortage, or exact match.
10. Calculate total expected revenue, total collected revenue, and overall discrepancy.
11. Display the route-wise reconciliation report.
12. Stop the program.

## 3. Flowchart (Mermaid TD)

\#chatgpt-mermaid-\_r_ka\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_ka\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ka\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_ka\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_ka\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ka\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_ka\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_ka\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_ka\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_ka\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_ka\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_ka\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ka\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ka\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_ka\_ p{margin:0;}#chatgpt-mermaid-\_r_ka\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ka\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ka\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ka\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_ka\_ .label text,#chatgpt-mermaid-\_r_ka\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ka\_ .node rect,#chatgpt-mermaid-\_r_ka\_ .node circle,#chatgpt-mermaid-\_r_ka\_ .node ellipse,#chatgpt-mermaid-\_r_ka\_ .node polygon,#chatgpt-mermaid-\_r_ka\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_ka\_ .rough-node .label text,#chatgpt-mermaid-\_r_ka\_ .node .label text,#chatgpt-mermaid-\_r_ka\_ .image-shape .label,#chatgpt-mermaid-\_r_ka\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_ka\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_ka\_ .rough-node .label,#chatgpt-mermaid-\_r_ka\_ .node .label,#chatgpt-mermaid-\_r_ka\_ .image-shape .label,#chatgpt-mermaid-\_r_ka\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_ka\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_ka\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ka\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ka\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_ka\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_ka\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_ka\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_ka\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_ka\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_ka\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_ka\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ka\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ka\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_ka\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_ka\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_ka\_ .icon-shape,#chatgpt-mermaid-\_r_ka\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_ka\_ .icon-shape p,#chatgpt-mermaid-\_r_ka\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_ka\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_ka\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_ka\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_ka\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_ka\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_ka\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_ka\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_ka\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_ka\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ka\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_ka\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_ka\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_ka\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_ka\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_ka\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_ka\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_ka\_ .node rect,#chatgpt-mermaid-\_r_ka\_ .node circle,#chatgpt-mermaid-\_r_ka\_ .node ellipse,#chatgpt-mermaid-\_r_ka\_ .node polygon,#chatgpt-mermaid-\_r_ka\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_ka\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_ka\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_ka\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_ka\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_ka\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of routesInput route name and basefareInput adult, student and seniorticketsCalculate discounted faresCalculate expected revenueInput collected revenueCalculate discrepancyMore routes?Calculate overall totalsDisplay reconciliation reportStopYesNo

## 4. Python Source Code

```
    if base_fare < 0:        print("Fare cannot be negative.")        raise SystemExit    adults = int(input("Enter adult tickets sold: "))    students = int(input("Enter student tickets sold: "))    seniors = int(input("Enter senior citizen tickets sold: "))    if adults < 0 or students < 0 or seniors < 0:        print("Ticket quantities cannot be negative.")        raise SystemExit    collected = float(        input("Enter actual collected revenue: Rs. ")    )    if collected < 0:        print("Revenue cannot be negative.")        raise SystemExit    # Calculate discounted fares    adult_fare = base_fare    student_fare = base_fare * (1 - STUDENT_DISCOUNT)    senior_fare = base_fare * (1 - SENIOR_DISCOUNT)    # Calculate expected revenue    adult_revenue = adults * adult_fare    student_revenue = students * student_fare    senior_revenue = seniors * senior_fare    expected = (        adult_revenue + student_revenue + senior_revenue    )    # Reconcile revenue    discrepancy = collected - expected    if discrepancy > 0:        status = "Excess collection"    elif discrepancy < 0:        status = "Revenue shortage"    else:        status = "Exact match"    routes.append({        "name": route_name,        "adults": adults,        "students": students,        "seniors": seniors,        "expected": expected,        "collected": collected,        "discrepancy": discrepancy,        "status": status    })# Display route-wise reportprint("\n===== FARE RECONCILIATION REPORT =====")for route in routes:    print(f"\nRoute: {route['name']}")    print(f"Adult tickets: {route['adults']}")    print(f"Student tickets: {route['students']}")    print(f"Senior citizen tickets: {route['seniors']}")    print(f"Expected revenue: Rs. {route['expected']:.2f}")    print(f"Collected revenue: Rs. {route['collected']:.2f}")    print(f"Discrepancy: Rs. {route['discrepancy']:.2f}")    print(f"Status: {route['status']}")
```

## 5. Sample Input

```

Enter number of routes: 2

Route 1
Enter route name: City-A
Enter base fare: Rs. 40
Enter adult tickets sold: 10
Enter student tickets sold: 4
Enter senior citizen tickets sold: 2
Enter actual collected revenue: Rs. 560

Route 2
Enter route name: City-B
Enter base fare: Rs. 60
Enter adult tickets sold: 8
Enter student tickets sold: 5
Enter senior citizen tickets sold: 3
Enter actual collected revenue: Rs. 830

```

## 6. Sample Output

```

===== FARE RECONCILIATION REPORT =====

Route: City-A
Adult tickets: 10
Student tickets: 4
Senior citizen tickets: 2
Expected revenue: Rs. 568.00
Collected revenue: Rs. 560.00
Discrepancy: Rs. -8.00
Status: Revenue shortage

Route: City-B
Adult tickets: 8
Student tickets: 5
Senior citizen tickets: 3
Expected revenue: Rs. 813.00
Collected revenue: Rs. 830.00
Discrepancy: Rs. 17.00
Status: Excess collection

===== OVERALL SUMMARY =====
Total expected revenue: Rs. 1381.00
Total collected revenue: Rs. 1390.00
Overall discrepancy: Rs. 9.00
Overall status: Excess collection

```

## 7. Result

The program calculates passenger fares using category-based discounts, determines expected revenue for each route, compares it with actual collections, and identifies revenue shortages or excess collections. The overall reconciliation report helps transport authorities monitor fare collection and detect discrepancies.
