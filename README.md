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

## AI Usage 
AI chatbot: Copilot was used to partially code some of the application's modules. Specifically: renderer.py, optimizer.py,
summarizer.py, and main.py. That was mainly for the purpose of producing correct and eaisly read formatting of the results. 
In the rest of the modules, Copilot was used to simplify the meaning of occurring errors and to recall some forgotton concepts. 

🧩 Example Input
Code
3x pipes to site B asap; deliver gloves (2 boxes) + 1 helmet to A tomorrow am; URGENT cement to site D; pickup empty pallets from C; H needs 5 vests by end of day

## 📄 Example Output (Structured)
Stop    | Item          | Quantity | Priority | When       
--------+---------------+----------+----------+------------

site B  | pipes         | 3        | High     | ASAP      

deliver | gloves        | 2        | Medium   | ASAP    

A       | helmet        | 1        | Medium   | Tomorrow AM

site D  | cement        |          | High     | ASAP       

C       | empty pallets |          | Medium   | ASAP     

H       | vests         | 5        | High     | End of Day 



## 🏗️ Project Structure
preprocessor.py

extracter.py

prioritizer.py

sorter.py

renderer.py

optimizer.py

summarizer.py

main.py

## 🚀 How It Works
1. Preprocess text  
Normalize separators, split into job segments.

2. Extract fields  
Uses an AI model to detect:
 - stop
 - item
 - quantity
 - priority keywords
 - time expressions

3. Score urgency  
Convert keywords like URGENT, asap, tomorrow into numeric priority.

4. Sort jobs  
Highest priority first,based on the priorities output.

5. Render table  
Display clean, consistent columns.

6. Bonus additions: 
  - Route optimizer: Finds a good route for the employees to take by weighting the distance and priorities. 
  - Summarizer: Provides a human readable summary of all the information found. 
  
## ⭐ Additional Details: 
### Run: 
You can run the application's entire pipeline by running the main module. 
Make sure to set your own enviroment variables for the API connection for a smooth run.
