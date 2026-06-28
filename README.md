# OrderOrganizer
A tool that reads messy logistics text and converts it into a clean, structured delivery plan. It extracts stops, items, quantities, priorities, and timing, then displays the results in a sorted table. Optionally, it computes an optimized visiting route using coordinates.

## 📌 Features
Parse messy free‑text logistics orders
- Extract:
  - Stop
  - Item
  - Quantity
  - Priority
  - When
- Sort jobs by urgency
- Display results in a clean table


## 🧩 Example Input
Code
3x pipes to site B asap; deliver gloves (2 boxes) + 1 helmet to A tomorrow am; URGENT cement to site D; pickup empty pallets from C; H needs 5 vests by end of day

## 📄 Example Output (Structured)
Stop	Item	Quantity	Priority	When
D	Cement	1	High	ASAP
B	Pipes	3	High	ASAP
A	Gloves	2 boxes	Medium	Tomorrow AM
A	Helmet	1	Medium	Tomorrow AM
H	Vests	5	Medium	End of Day
C	Empty Pallets	—	Low	—

## 🏗️ Project Structure
TBA

## 🚀 How It Works
1. Preprocess text  
Normalize separators, split into job segments.

2. Extract fields  
Use rule-based parsing or an AI model to detect:
 - stop
 - item
 - quantity
 - priority keywords
 - time expressions

3. Score urgency  
Convert keywords like URGENT, asap, tomorrow into numeric priority.

4. Sort jobs  
Highest priority first.

5. Render table  
Display clean, consistent columns.
