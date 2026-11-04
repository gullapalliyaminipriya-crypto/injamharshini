

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
## 3. flowchart(mermaid TD)
```mermaid
flowchart TD
    A([Start]) --> B[/Enter passenger details/]
    B --> C[/Select route and passenger category/]
    C --> D[Calculate fare based on route]
    D --> E[Apply passenger category discount]
    E --> F[Calculate total expected revenue]
    F --> G[/Enter actual collected revenue/]
    G --> H[Compare expected and collected revenue]
    H --> I{Are both amounts equal?}
    I -->|Yes| J[Display No Discrepancy]
    I -->|No| K[Calculate Revenue Difference]
    K --> L[Identify Revenue Discrepancy]
    J --> M[Generate Fare Reconciliation Report]
    L --> M
    M --> N([End])
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


