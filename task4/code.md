# Integrated Warehouse Order Prioritization

## 1. Problem Statement

Develop a Python program to manage and prioritize customer orders in a warehouse. The program should process product demand, available stock levels, order quantities, and priority categories. It must allocate stock to orders according to their priority, determine whether each order can be fully or partially fulfilled, and calculate outstanding quantities for unfulfilled orders.

Assumptions used:

- Each product has a fixed available stock.
- Orders are classified as High, Medium, or Low priority.
- High-priority orders are processed first, followed by Medium and Low.
- Orders with the same priority are processed in their input order.
- Stock cannot become negative.
- Outstanding quantity = Ordered quantity − Fulfilled quantity.

## 2. Algorithm

1. Start the program.
2. Input the number of products and their available stock levels.
3. Input the number of customer orders.
4. For each order, input the order ID, product name, quantity, and priority category.
5. Sort orders by priority: High, Medium, then Low.
6. Check whether the requested product exists in the warehouse.
7. Allocate available stock to each order, without exceeding the requested quantity.
8. Determine whether the order is fully fulfilled, partially fulfilled, or unfulfilled.
9. Calculate the outstanding quantity for every order.
10. Display the order fulfilment report and remaining stock.
11. Stop the program.

## 3. Flowchart (Mermaid TD)

\#chatgpt-mermaid-\_r_q7\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_q7\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_q7\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_q7\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_q7\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_q7\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_q7\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_q7\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_q7\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_q7\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_q7\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_q7\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_q7\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_q7\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_q7\_ p{margin:0;}#chatgpt-mermaid-\_r_q7\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_q7\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_q7\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_q7\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_q7\_ .label text,#chatgpt-mermaid-\_r_q7\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_q7\_ .node rect,#chatgpt-mermaid-\_r_q7\_ .node circle,#chatgpt-mermaid-\_r_q7\_ .node ellipse,#chatgpt-mermaid-\_r_q7\_ .node polygon,#chatgpt-mermaid-\_r_q7\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_q7\_ .rough-node .label text,#chatgpt-mermaid-\_r_q7\_ .node .label text,#chatgpt-mermaid-\_r_q7\_ .image-shape .label,#chatgpt-mermaid-\_r_q7\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_q7\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_q7\_ .rough-node .label,#chatgpt-mermaid-\_r_q7\_ .node .label,#chatgpt-mermaid-\_r_q7\_ .image-shape .label,#chatgpt-mermaid-\_r_q7\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_q7\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_q7\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_q7\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_q7\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_q7\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_q7\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_q7\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_q7\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_q7\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_q7\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_q7\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_q7\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_q7\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_q7\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_q7\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_q7\_ .icon-shape,#chatgpt-mermaid-\_r_q7\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_q7\_ .icon-shape p,#chatgpt-mermaid-\_r_q7\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_q7\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_q7\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_q7\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_q7\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_q7\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_q7\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_q7\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_q7\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_q7\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_q7\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_q7\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_q7\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_q7\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_q7\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_q7\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_q7\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_q7\_ .node rect,#chatgpt-mermaid-\_r_q7\_ .node circle,#chatgpt-mermaid-\_r_q7\_ .node ellipse,#chatgpt-mermaid-\_r_q7\_ .node polygon,#chatgpt-mermaid-\_r_q7\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_q7\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_q7\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_q7\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_q7\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_q7\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput products and stock levelsInput customer orders andprioritiesSort orders by prioritySelect next orderProduct available?Set fulfilled quantity to zeroAllocate available stockCalculate outstanding quantityMore orders?Display fulfilment reportDisplay remaining stockStopNoYesYesNo

## 4. Python Source Code

```
        fulfilled = min(requested, stock[product])        stock[product] -= fulfilled        if fulfilled == requested:            status = "Fully fulfilled"        elif fulfilled > 0:            status = "Partially fulfilled"        else:            status = "Unfulfilled"    outstanding = requested - fulfilled    report.append({        **order,        "fulfilled": fulfilled,        "outstanding": outstanding,        "status": status    })# Display fulfilment reportprint("\n===== ORDER FULFILMENT REPORT =====")for order in report:    print(f"\nOrder ID: {order['id']}")    print(f"Product: {order['product']}")    print(f"Priority: {order['priority']}")    print(f"Ordered quantity: {order['quantity']}")    print(f"Fulfilled quantity: {order['fulfilled']}")    print(f"Outstanding quantity: {order['outstanding']}")    print(f"Status: {order['status']}")# Display remaining stockprint("\n===== REMAINING WAREHOUSE STOCK =====")for product, quantity in stock.items():    print(f"{product}: {quantity} units")total_ordered = sum(o["quantity"] for o in report)total_fulfilled = sum(o["fulfilled"] for o in report)total_outstanding = sum(o["outstanding"] for o in report)print("\n===== SUMMARY =====")print("Total quantity ordered:", total_ordered)print("Total quantity fulfilled:", total_fulfilled)print("Total outstanding quantity:", total_outstanding)
```

## 5. Sample Input

```

Enter number of products: 2
Enter product name: Pen
Enter available stock: 10
Enter product name: Notebook
Enter available stock: 5

Enter number of orders: 4

Order 1
Enter order ID: O101
Enter product name: Pen
Enter order quantity: 7
Enter priority (High/Medium/Low): High

Order 2
Enter order ID: O102
Enter product name: Pen
Enter order quantity: 6
Enter priority (High/Medium/Low): Low

Order 3
Enter order ID: O103
Enter product name: Notebook
Enter order quantity: 8
Enter priority (High/Medium/Low): Medium

Order 4
Enter order ID: O104
Enter product name: Notebook
Enter order quantity: 3
Enter priority (High/Medium/Low): High

```

## 6. Sample Output

```

===== ORDER FULFILMENT REPORT =====

Order ID: O101
Product: Pen
Priority: High
Ordered quantity: 7
Fulfilled quantity: 7
Outstanding quantity: 0
Status: Fully fulfilled

Order ID: O104
Product: Notebook
Priority: High
Ordered quantity: 3
Fulfilled quantity: 3
Outstanding quantity: 0
Status: Fully fulfilled

Order ID: O103
Product: Notebook
Priority: Medium
Ordered quantity: 8
Fulfilled quantity: 2
Outstanding quantity: 6
Status: Partially fulfilled

Order ID: O102
Product: Pen
Priority: Low
Ordered quantity: 6
Fulfilled quantity: 3
Outstanding quantity: 3
Status: Partially fulfilled

===== REMAINING WAREHOUSE STOCK =====
Pen: 0 units
Notebook: 0 units

===== SUMMARY =====
Total quantity ordered: 24
Total quantity fulfilled: 15
Total outstanding quantity: 9

```

## 7. Result

The program prioritizes orders according to their priority categories, allocates available stock without exceeding inventory limits, and identifies fully fulfilled, partially fulfilled, and unfulfilled orders. It also calculates the outstanding quantities and displays the remaining warehouse stock.
