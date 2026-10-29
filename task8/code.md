# Manufacturing Quality Control Matrix – Python Project

## 1. Problem Statement

Develop a Python program to analyse production quantities and defective units across multiple products and batches using a matrix (nested list). The program must calculate the defect percentage for each batch, compare it with a specified quality threshold, identify batches that exceed the threshold, and display a final quality control report.

Assumptions:

- Each batch contains the production quantity and number of defective units.
- Defective units cannot exceed the production quantity.
- The quality threshold is 5%.
- A batch is marked Needs Inspection if its defect percentage is greater than 5%; otherwise, it is marked Acceptable.

## 2. Algorithm

1. Start the program.
2. Input the number of products and batches.
3. Input the product name, production quantity, and defective units for each batch.
4. Store the batch data in a nested list.
5. Calculate the defect percentage using:

\\[ \text{Defect Percentage}= \frac{\text{Defective Units}}{\text{Production Quantity}}\times100 \\]

6. Compare each batch's defect percentage with the quality threshold.
7. Identify batches exceeding the threshold.
8. Display the quality control report and summary.
9. Stop the program.

## 3. Flowchart

\#chatgpt-mermaid-\_r_13i\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_13i\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_13i\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_13i\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_13i\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_13i\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_13i\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_13i\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_13i\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_13i\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_13i\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_13i\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_13i\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_13i\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_13i\_ p{margin:0;}#chatgpt-mermaid-\_r_13i\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_13i\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_13i\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_13i\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_13i\_ .label text,#chatgpt-mermaid-\_r_13i\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_13i\_ .node rect,#chatgpt-mermaid-\_r_13i\_ .node circle,#chatgpt-mermaid-\_r_13i\_ .node ellipse,#chatgpt-mermaid-\_r_13i\_ .node polygon,#chatgpt-mermaid-\_r_13i\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_13i\_ .rough-node .label text,#chatgpt-mermaid-\_r_13i\_ .node .label text,#chatgpt-mermaid-\_r_13i\_ .image-shape .label,#chatgpt-mermaid-\_r_13i\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_13i\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_13i\_ .rough-node .label,#chatgpt-mermaid-\_r_13i\_ .node .label,#chatgpt-mermaid-\_r_13i\_ .image-shape .label,#chatgpt-mermaid-\_r_13i\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_13i\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_13i\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_13i\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_13i\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_13i\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_13i\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_13i\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_13i\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_13i\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_13i\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_13i\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_13i\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_13i\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_13i\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_13i\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_13i\_ .icon-shape,#chatgpt-mermaid-\_r_13i\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_13i\_ .icon-shape p,#chatgpt-mermaid-\_r_13i\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_13i\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_13i\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_13i\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_13i\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_13i\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_13i\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_13i\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_13i\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_13i\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_13i\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_13i\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_13i\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_13i\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_13i\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_13i\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_13i\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_13i\_ .node rect,#chatgpt-mermaid-\_r_13i\_ .node circle,#chatgpt-mermaid-\_r_13i\_ .node ellipse,#chatgpt-mermaid-\_r_13i\_ .node polygon,#chatgpt-mermaid-\_r_13i\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_13i\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_13i\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_13i\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_13i\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_13i\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput number of products andbatchesInput product name,production quantity anddefective unitsStore batch data in nested listMore batches?Calculate defect percentageDefect percentage greater than5%?Mark Needs InspectionMark AcceptableMore batches to analyse?Display quality control reportStopYesNoYesNoYesNo

## 4. Python Source Code

```
    for j in range(batches_count):        print(f"Batch {j + 1}")        quantity = int(input("Enter production quantity: "))        defective = int(input("Enter defective units: "))        if quantity <= 0 or defective < 0 or defective > quantity:            print("Invalid production or defective quantity.")            raise SystemExit        batches.append([quantity, defective])    products.append([product_name, batches])print("\n======= QUALITY CONTROL REPORT =======")print("Threshold:", quality_threshold, "%")inspection_count = 0total_produced = 0total_defective = 0for product in products:    product_name = product[0]    batches = product[1]    print(f"\nProduct: {product_name}")    for i, batch in enumerate(batches, start=1):        quantity = batch[0]        defective = batch[1]        defect_percentage = defective / quantity * 100        total_produced += quantity        total_defective += defective        if defect_percentage > quality_threshold:            status = "Needs Inspection"            inspection_count += 1        else:            status = "Acceptable"        print(            f"Batch {i}: Produced={quantity}, "            f"Defective={defective}, "            f"Defect={defect_percentage:.2f}%, "            f"Status={status}"        )print("\n======= OVERALL SUMMARY =======")print("Total production:", total_produced)print("Total defective units:", total_defective)if total_produced > 0:    overall_percentage = total_defective / total_produced * 100    print(f"Overall defect percentage: {overall_percentage:.2f}%")print("Batches needing inspection:", inspection_count)
```

## 5. Sample Input

```

Enter number of products: 2

Enter product name: Laptop
Enter number of batches: 2
Batch 1
Enter production quantity: 100
Enter defective units: 3
Batch 2
Enter production quantity: 200
Enter defective units: 15

Enter product name: Keyboard
Enter number of batches: 2
Batch 1
Enter production quantity: 150
Enter defective units: 12
Batch 2
Enter production quantity: 100
Enter defective units: 2

```

## 6. Sample Output

```

======= QUALITY CONTROL REPORT =======
Threshold: 5.0 %

Product: Laptop
Batch 1: Produced=100, Defective=3, Defect=3.00%, Status=Acceptable
Batch 2: Produced=200, Defective=15, Defect=7.50%, Status=Needs Inspection

Product: Keyboard
Batch 1: Produced=150, Defective=12, Defect=8.00%, Status=Needs Inspection
Batch 2: Produced=100, Defective=2, Defect=2.00%, Status=Acceptable

======= OVERALL SUMMARY =======
Total production: 550
Total defective units: 32
Overall defect percentage: 5.82%
Batches needing inspection: 2

```

## 7. Result

The Python program successfully stores production data in nested lists, calculates defect percentages for each batch, identifies batches exceeding the 5% quality threshold, and displays the overall manufacturing quality report.
