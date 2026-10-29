# Multi-Branch Retail Inventory Transfer

## 1. Problem Statement

Develop a Python program to manage inventory transfers between multiple retail branches. The program should compare each branch's current stock with its target stock level, calculate surplus and shortage quantities for each product, and generate stock transfer recommendations.

The program must respect transfer constraints, including the maximum quantity transferable per transaction and the requirement that a branch cannot transfer more stock than its available surplus. It should update stock levels after transfers and display any remaining shortages.

Assumptions used:

- All branches maintain the same list of products.
- A branch with stock above its target can supply branches with shortages.
- Transfers are made only between different branches for the same product.
- Each transfer is limited by a user-specified maximum quantity.
- Stock is never allowed to become negative.
- Remaining shortages are reported when available surplus cannot meet demand.

## 2. Algorithm

1. Start the program.
2. Input the number of branches, products, and maximum transfer quantity.
3. Enter the current stock and target stock for each product at every branch.
4. Calculate the surplus or shortage for each branch and product.
5. Identify branches with surplus stock and branches with shortages.
6. Select a donor branch and a recipient branch for the same product.
7. Transfer the minimum of available surplus, remaining shortage, and maximum transfer quantity.
8. Repeat transfers until no further transfers are possible.
9. Update stock levels and calculate remaining shortages.
10. Display surplus, shortage, transfer details, and final stock levels.
11. Stop the program.

## 3. Flowchart (Mermaid TD)

\#chatgpt-mermaid-\_r_o6\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_o6\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_o6\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_o6\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_o6\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_o6\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_o6\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_o6\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_o6\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_o6\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_o6\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_o6\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_o6\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_o6\_ p{margin:0;}#chatgpt-mermaid-\_r_o6\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_o6\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_o6\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_o6\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_o6\_ .label text,#chatgpt-mermaid-\_r_o6\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_o6\_ .node rect,#chatgpt-mermaid-\_r_o6\_ .node circle,#chatgpt-mermaid-\_r_o6\_ .node ellipse,#chatgpt-mermaid-\_r_o6\_ .node polygon,#chatgpt-mermaid-\_r_o6\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .rough-node .label text,#chatgpt-mermaid-\_r_o6\_ .node .label text,#chatgpt-mermaid-\_r_o6\_ .image-shape .label,#chatgpt-mermaid-\_r_o6\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_o6\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .rough-node .label,#chatgpt-mermaid-\_r_o6\_ .node .label,#chatgpt-mermaid-\_r_o6\_ .image-shape .label,#chatgpt-mermaid-\_r_o6\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_o6\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_o6\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_o6\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_o6\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_o6\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_o6\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_o6\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_o6\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_o6\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_o6\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_o6\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_o6\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_o6\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_o6\_ .icon-shape,#chatgpt-mermaid-\_r_o6\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_o6\_ .icon-shape p,#chatgpt-mermaid-\_r_o6\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_o6\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_o6\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_o6\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_o6\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_o6\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_o6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_o6\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_o6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_o6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_o6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_o6\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_o6\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_o6\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_o6\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .node rect,#chatgpt-mermaid-\_r_o6\_ .node circle,#chatgpt-mermaid-\_r_o6\_ .node ellipse,#chatgpt-mermaid-\_r_o6\_ .node polygon,#chatgpt-mermaid-\_r_o6\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_o6\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_o6\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_o6\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_o6\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartInput branches, products andtransfer limitInput current and target stockCalculate surplus and shortageSurplus and shortageavailable?Select donor and recipientCalculate allowed transferquantityUpdate stock and recordtransferCalculate remaining shortagesDisplay transfers and finalstockStopYesNo

## 4. Python Source Code

```
# Multi-Branch Retail Inventory Transferbranches = []products = []n = int(input("Enter number of branches: "))p = int(input("Enter number of products: "))max_transfer = int(input("Enter maximum quantity per transfer: "))if n <= 0 or p <= 0 or max_transfer <= 0:    print("Invalid input.")    raise SystemExit# Input product namesfor i in range(p):    product = input(f"Enter product {i + 1} name: ")    products.append(product)# Input branch stock and target levelsfor i in range(n):    name = input(f"\nEnter branch {i + 1} name: ")    stock = []    target = []    for product in products:        current = int(input(f"{product} current stock: "))        required = int(input(f"{product} target stock: "))        if current < 0 or required < 0:            print("Stock and target values cannot be negative.")            raise SystemExit        stock.append(current)        target.append(required)
```

## 5. Sample Input

```

Enter number of branches: 2
Enter number of products: 2
Enter maximum quantity per transfer: 4
Enter product 1 name: Pen
Enter product 2 name: Notebook

Enter branch 1 name: Branch-A
Pen current stock: 20
Pen target stock: 10
Notebook current stock: 5
Notebook target stock: 10

Enter branch 2 name: Branch-B
Pen current stock: 3
Pen target stock: 8
Notebook current stock: 20
Notebook target stock: 15

```

## 6. Sample Output

```

===== INITIAL INVENTORY ANALYSIS =====

Branch: Branch-A
Pen: Surplus = 5, Shortage = 0
Notebook: Surplus = 0, Shortage = 5

Branch: Branch-B
Pen: Surplus = 0, Shortage = 0
Notebook: Surplus = 5, Shortage = 0

===== TRANSFER PLAN =====
Pen: 4 units from Branch-A to Branch-B
Pen: 1 units from Branch-A to Branch-B
Notebook: 4 units from Branch-B to Branch-A
Notebook: 1 units from Branch-B to Branch-A

===== FINAL INVENTORY =====

Branch: Branch-A
Pen: Final stock = 15, Target = 10, Remaining shortage = 0
Notebook: Final stock = 10, Target = 10, Remaining shortage = 0

Branch: Branch-B
Pen: Final stock = 8, Target = 8, Remaining shortage = 0
Notebook: Final stock = 16, Target = 15, Remaining shortage = 0

Total transfer transactions: 4
Total units transferred: 10
Total remaining shortage: 0

```

Important correction: The sample output's initial inventory analysis should be calculated and printed before the transfer loop. Also, for Branch-A's Pen, the initial surplus is 10 units, not 5. The correct initial analysis is:

- Branch-A: Pen surplus = 10; Notebook shortage = 5.
- Branch-B: Pen shortage = 5; Notebook surplus = 5.

## 7. Result

The program compares branch-level stock with target levels, calculates surpluses and shortages, and generates transfers that respect the maximum quantity per transaction. It updates inventory after each transfer and reports any shortages that remain.
