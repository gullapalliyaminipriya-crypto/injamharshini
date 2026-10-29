# Energy Conservation Before-and-After Analysis

## 1. Problem Statement

Develop a Python program to analyse electricity consumption of different appliances before and after an energy conservation intervention. The program should calculate energy savings, savings percentages, total electricity savings, and rank appliances according to the amount of electricity saved.

Assumptions used:

- Electricity usage is measured in kilowatt-hours (kWh).
- Savings = Before-intervention usage − After-intervention usage.
- Savings percentage = (Savings ÷ Before-intervention usage) × 100.
- Appliances are ranked from highest to lowest savings.
- If initial usage is zero, the savings percentage is reported as undefined.
- Negative savings indicate increased electricity consumption.

## 2. Algorithm

1. Start the program.
2. Input the number of appliances.
3. Enter each appliance name and its electricity usage before and after the intervention.
4. Validate that usage values are non-negative.
5. Calculate savings for each appliance.
6. Calculate the savings percentage.
7. Calculate total electricity usage before and after the intervention.
8. Calculate total energy savings and overall savings percentage.
9. Rank appliances by electricity savings in descending order.
10. Display the appliance-wise analysis and final ranking.
11. Stop the program.

## 3. Flowchart (Mermaid TD)

\#chatgpt-mermaid-\_r_u4\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_u4\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_u4\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_u4\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_u4\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_u4\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_u4\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_u4\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_u4\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_u4\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_u4\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_u4\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_u4\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_u4\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_u4\_ p{margin:0;}#chatgpt-mermaid-\_r_u4\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_u4\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_u4\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_u4\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_u4\_ .label text,#chatgpt-mermaid-\_r_u4\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_u4\_ .node rect,#chatgpt-mermaid-\_r_u4\_ .node circle,#chatgpt-mermaid-\_r_u4\_ .node ellipse,#chatgpt-mermaid-\_r_u4\_ .node polygon,#chatgpt-mermaid-\_r_u4\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_u4\_ .rough-node .label text,#chatgpt-mermaid-\_r_u4\_ .node .label text,#chatgpt-mermaid-\_r_u4\_ .image-shape .label,#chatgpt-mermaid-\_r_u4\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_u4\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_u4\_ .rough-node .label,#chatgpt-mermaid-\_r_u4\_ .node .label,#chatgpt-mermaid-\_r_u4\_ .image-shape .label,#chatgpt-mermaid-\_r_u4\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_u4\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_u4\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_u4\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_u4\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_u4\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_u4\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_u4\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_u4\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_u4\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_u4\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_u4\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_u4\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_u4\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_u4\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_u4\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_u4\_ .icon-shape,#chatgpt-mermaid-\_r_u4\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_u4\_ .icon-shape p,#chatgpt-mermaid-\_r_u4\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_u4\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_u4\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_u4\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_u4\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_u4\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_u4\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_u4\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_u4\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_u4\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_u4\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_u4\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_u4\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_u4\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_u4\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_u4\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_u4\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_u4\_ .node rect,#chatgpt-mermaid-\_r_u4\_ .node circle,#chatgpt-mermaid-\_r_u4\_ .node ellipse,#chatgpt-mermaid-\_r_u4\_ .node polygon,#chatgpt-mermaid-\_r_u4\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_u4\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_u4\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_u4\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_u4\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_u4\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of appliancesInput appliance name andbefore-after usageValidate usage valuesCalculate energy savingsCalculate savings percentageMore appliances?Calculate total energy savingsRank appliances by savingsDisplay analysis and rankingStopYesNo

## 4. Python Source Code

```
# Energy Conservation Before-and-After Analysisappliances = []n = int(input("Enter number of appliances: "))if n <= 0:    print("Invalid number of appliances.")    raise SystemExitfor i in range(n):    print(f"\nAppliance {i + 1}")    name = input("Enter appliance name: ").strip()    before = float(input("Enter usage before intervention (kWh): "))    after = float(input("Enter usage after intervention (kWh): "))    if not name or before < 0 or after < 0:        print("Invalid name or usage value.")        raise SystemExit    savings = before - after    if before > 0:        percentage = (savings / before) * 100    else:        percentage = None    if savings > 0:        status = "Energy saved"    elif savings < 0:        status = "Consumption increased"    else:        status = "No change"
```

## 5. Sample Input

```

Enter number of appliances: 4

Appliance 1
Enter appliance name: Fan
Enter usage before intervention (kWh): 120
Enter usage after intervention (kWh): 80

Appliance 2
Enter appliance name: AC
Enter usage before intervention (kWh): 300
Enter usage after intervention (kWh): 210

Appliance 3
Enter appliance name: Lights
Enter usage before intervention (kWh): 100
Enter usage after intervention (kWh): 60

Appliance 4
Enter appliance name: Refrigerator
Enter usage before intervention (kWh): 150
Enter usage after intervention (kWh): 135

```

## 6. Sample Output

```

===== ENERGY CONSERVATION REPORT =====

Appliance: Fan
Before usage: 120.00 kWh
After usage: 80.00 kWh
Energy savings: 40.00 kWh
Savings percentage: 33.33%
Status: Energy saved

Appliance: AC
Before usage: 300.00 kWh
After usage: 210.00 kWh
Energy savings: 90.00 kWh
Savings percentage: 30.00%
Status: Energy saved

Appliance: Lights
Before usage: 100.00 kWh
After usage: 60.00 kWh
Energy savings: 40.00 kWh
Savings percentage: 40.00%
Status: Energy saved

Appliance: Refrigerator
Before usage: 150.00 kWh
After usage: 135.00 kWh
Energy savings: 15.00 kWh
Savings percentage: 10.00%
Status: Energy saved

===== APPLIANCE SAVINGS RANKING =====
1. AC - 90.00 kWh saved
2. Fan - 40.00 kWh saved
3. Lights - 40.00 kWh saved
4. Refrigerator - 15.00 kWh saved

===== OVERALL SUMMARY =====
Total before usage: 670.00 kWh
Total after usage: 485.00 kWh
Total energy savings: 185.00 kWh
Overall savings percentage: 27.61%
Overall result: Energy consumption reduced

```

## 7. Result

The program compares appliance-wise electricity usage before and after an intervention, calculates energy savings and savings percentages, and ranks appliances by achieved savings. In this example, the campus saves 185 kWh, achieving an overall electricity consumption reduction of 27.61%.
