# Integrated Campus Energy and Water Audit

## 1. Problem Statement

Develop a Python program to analyse electricity and water consumption across multiple campus buildings over several days. The program should calculate the total consumption and cost for each building, determine the percentage change between the first and last day, identify buildings with excessive consumption, and rank buildings using a specified scoring method.

The program uses lists, nested lists, loops, conditional statements, and arithmetic operations to generate an energy and water audit report.

Assumptions used in this program:

- Electricity cost = ₹8 per unit (kWh).
- Water cost = ₹30 per kilolitre (kL).
- Excessive consumption is identified when the average daily usage exceeds the specified limits.
- Building score = 60% electricity usage score + 40% water usage score, with lower consumption receiving a better rank.

## 2. Algorithm

1. Start the program.
2. Read the number of buildings and the number of days.
3. Input the building names and daily electricity and water consumption.
4. Calculate the total and average consumption for each building.
5. Calculate electricity cost, water cost, and total cost.
6. Calculate the percentage change from the first day to the last day.
7. Check whether electricity or water consumption exceeds the specified limits.
8. Calculate a combined score for each building using electricity and water consumption.
9. Rank buildings from lowest to highest score.
10. Display consumption, costs, percentage changes, excessive consumption warnings, and rankings.
11. Stop the program.

## 3. Flowchart (Mermaid TD)

\#chatgpt-mermaid-\_r_i5\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_i5\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_i5\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_i5\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_i5\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_i5\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_i5\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_i5\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_i5\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_i5\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_i5\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_i5\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_i5\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_i5\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_i5\_ p{margin:0;}#chatgpt-mermaid-\_r_i5\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_i5\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_i5\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_i5\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_i5\_ .label text,#chatgpt-mermaid-\_r_i5\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_i5\_ .node rect,#chatgpt-mermaid-\_r_i5\_ .node circle,#chatgpt-mermaid-\_r_i5\_ .node ellipse,#chatgpt-mermaid-\_r_i5\_ .node polygon,#chatgpt-mermaid-\_r_i5\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_i5\_ .rough-node .label text,#chatgpt-mermaid-\_r_i5\_ .node .label text,#chatgpt-mermaid-\_r_i5\_ .image-shape .label,#chatgpt-mermaid-\_r_i5\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_i5\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_i5\_ .rough-node .label,#chatgpt-mermaid-\_r_i5\_ .node .label,#chatgpt-mermaid-\_r_i5\_ .image-shape .label,#chatgpt-mermaid-\_r_i5\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_i5\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_i5\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_i5\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_i5\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_i5\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_i5\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_i5\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_i5\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_i5\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_i5\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_i5\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_i5\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_i5\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_i5\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_i5\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_i5\_ .icon-shape,#chatgpt-mermaid-\_r_i5\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_i5\_ .icon-shape p,#chatgpt-mermaid-\_r_i5\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_i5\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_i5\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_i5\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_i5\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_i5\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_i5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_i5\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_i5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_i5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_i5\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_i5\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_i5\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_i5\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_i5\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_i5\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_i5\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_i5\_ .node rect,#chatgpt-mermaid-\_r_i5\_ .node circle,#chatgpt-mermaid-\_r_i5\_ .node ellipse,#chatgpt-mermaid-\_r_i5\_ .node polygon,#chatgpt-mermaid-\_r_i5\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_i5\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_i5\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_i5\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_i5\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_i5\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of buildings anddaysInput building names and dailyconsumptionCalculate total and averageconsumptionCalculate electricity cost andwater costCalculate percentage changesConsumption above limits?Mark excessive consumptionMark normal consumptionCalculate combined scoreRank buildings by scoreDisplay audit report andrankingsStopYesNo

## 4. Python Source Code

```
    name = input("\nEnter building name: ")    electricity = []    water = []    for d in range(days):        e = float(input(            f"Day {d + 1} electricity (kWh): "        ))        w = float(input(            f"Day {d + 1} water (kL): "        ))        if e < 0 or w < 0:            print("Consumption cannot be negative.")            raise SystemExit        electricity.append(e)        water.append(w)    total_e = sum(electricity)    total_w = sum(water)    avg_e = total_e / days    avg_w = total_w / days    electricity_cost = total_e * ELECTRICITY_RATE    water_cost = total_w * WATER_RATE    total_cost = electricity_cost + water_cost    if electricity[0] != 0:        e_change = (            (electricity[-1] - electricity[0])            / electricity[0]        ) * 100    else:        e_change = 0 if electricity[-1] == 0 else None    if water[0] != 0:        w_change = (            (water[-1] - water[0]) / water[0]        ) * 100    else:        w_change = 0 if water[-1] == 0 else None    excessive = []    if avg_e > ELECTRICITY_LIMIT:        excessive.append("Electricity")    if avg_w > WATER_LIMIT:        excessive.append("Water")    # Lower consumption gives a lower score.    # Score = 60% electricity + 40% water.    score = (0.6 * avg_e / ELECTRICITY_LIMIT             + 0.4 * avg_w / WATER_LIMIT) * 100    buildings.append({        "name": name,        "total_e": total_e,        "total_w": total_w,        "avg_e": avg_e,        "avg_w": avg_w,        "electricity_cost": electricity_cost,        "water_cost": water_cost,        "total_cost": total_cost,        "e_change": e_change,        "w_change": w_change,        "excessive": excessive,        "score": score    })# Display individual building reportsprint("\n========== CAMPUS AUDIT REPORT ==========")
```

## 5. Sample Input

For this example, enter the following values in the same order as the program prompts.

```

Enter number of buildings: 3
Enter number of days: 2

Enter building name: Library
Day 1 electricity (kWh): 80
Day 1 water (kL): 5
Day 2 electricity (kWh): 90
Day 2 water (kL): 6

Enter building name: Laboratory
Day 1 electricity (kWh): 120
Day 1 water (kL): 12
Day 2 electricity (kWh): 140
Day 2 water (kL): 14

Enter building name: Hostel
Day 1 electricity (kWh): 100
Day 1 water (kL): 8
Day 2 electricity (kWh): 110
Day 2 water (kL): 9

```

## 6. Sample Output

```

========== CAMPUS AUDIT REPORT ==========

Building: Library
Total electricity: 170.00 kWh
Total water: 11.00 kL
Average electricity: 85.00 kWh/day
Average water: 5.50 kL/day
Electricity cost: Rs. 1360.00
Water cost: Rs. 330.00
Total cost: Rs. 1690.00
Electricity percentage change: 12.50%
Water percentage change: 20.00%
Consumption status: Normal
Combined score: 73.00

Building: Laboratory
Total electricity: 260.00 kWh
Total water: 26.00 kL
Average electricity: 130.00 kWh/day
Average water: 13.00 kL/day
Electricity cost: Rs. 2080.00
Water cost: Rs. 780.00
Total cost: Rs. 2860.00
Electricity percentage change: 16.67%
Water percentage change: 16.67%
Warning: Excessive Electricity, Water
Combined score: 130.00

Building: Hostel
Total electricity: 210.00 kWh
Total water: 17.00 kL
Average electricity: 105.00 kWh/day
Average water: 8.50 kL/day
Electricity cost: Rs. 1680.00
Water cost: Rs. 510.00
Total cost: Rs. 2190.00
Electricity percentage change: 10.00%
Water percentage change: 12.50%
Warning: Excessive Electricity
Combined score: 105.00

========== BUILDING RANKING ==========
1. Library - Score: 73.00
2. Hostel - Score: 105.00
3. Laboratory - Score: 130.00

========== CAMPUS TOTALS ==========
Total electricity: 640.00 kWh
Total water: 54.00 kL
Total expenditure: Rs. 6740.00

```

## 7. Result

The program successfully calculates electricity and water consumption, estimates costs, measures percentage changes, identifies excessive consumption, and ranks campus buildings. In this example, Library ranks first, while Laboratory requires attention because both its electricity and water usage exceed the defined limits.
