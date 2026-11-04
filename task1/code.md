

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
```mermaid
flowchart TD
    A([Start]) --> B[/Enter Two Numbers/]
    B --> C[Add Two Numbers]
    C --> D[Display Result]
    D --> E([End])

    style A fill:#90EE90,stroke:#008000
    style B fill:#87CEEB,stroke:#0000FF
    style C fill:#FFFF99,stroke:#DAA520
    style D fill:#FFB6C1,stroke:#FF1493
    style E fill:#90EE90,stroke:#008000
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
