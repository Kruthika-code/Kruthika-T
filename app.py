import os
import sys
import re
import time

# Starting maximum budgets for evaluation
food_budget = 1500.00
transport_budget = 150.00

# Wipes old logs so the dashboard stays neatly at the top
os.system('cls' if os.name == 'nt' else 'clear')

print("=" * 60)
print("         SMARTSPEND MULTI-ENTITY AI ENGINE (v2.0)          ")
print("  Developed for School Project Evaluation • Status: Running ")
print("=" * 60)

# AUTOMATIC TYPING FOCUS: The cursor flashes here instantly when you run the file
user_input = input("\n📝 Describe your expense(s) casually: ")

if user_input.strip():
    input_lower = user_input.lower()
    
    # Vocabulary lists for matching
    food_keywords = ['food', 'snacks', 'snack', 'lunch', 'dinner', 'breakfast', 'eat', 'hotel', 'burger', 'pizza', 'meals']
    transport_keywords = ['transport', 'travel', 'bus', 'auto', 'cab', 'bike', 'petrol', 'travel', 'fare', 'train', 'ticket', 'ride']
    
    # Advanced Parsing: Split the bulky sentence into pieces
    phrases = re.split(r'and|,|\.', input_lower)
    
    extracted_logs = []
    
    # Process each piece of the sentence individually
    for phrase in phrases:
        phrase = phrase.strip()
        if not phrase:
            continue
            
        # Find the number inside this specific phrase
        numbers = re.findall(r'\d+', phrase)
        if not numbers:
            continue
        amount = float(numbers[0])
        
        # Detect category for this specific phrase
        is_food = any(word in phrase for word in food_keywords)
        is_transport = any(word in phrase for word in transport_keywords)
        
        if is_food:
            food_budget -= amount
            extracted_logs.append(f" ✔️ Extracted: ₹{amount:.2f} routed to [Food Category]")
        elif is_transport:
            # Run the smart cross-category overflow math
            if amount > transport_budget:
                overflow = amount - transport_budget
                extracted_logs.append(f" ✔️ Extracted: ₹{amount:.2f} to [Transport] -> ⚠️ OVERFLOW: ₹{overflow:.2f} routed to Food")
                transport_budget = 0.0
                food_budget -= overflow
            else:
                transport_budget -= amount
                extracted_logs.append(f" ✔️ Extracted: ₹{amount:.2f} routed to [Transport Category]")
        else:
            extracted_logs.append(f" ✔️ Extracted: ₹{amount:.2f} routed to [General overhead]")
    
    # Print everything out cleanly at the end before terminating
    print("\n📢 TRANSACTION PROCESSING REPORT:")
    print("-" * 40)
    if extracted_logs:
        print("\n".join(extracted_logs))
    else:
        print(" -> Warning: No clear amount or category detected.")
    print("-" * 40)
    
    # LIVE LEDGER BUDGET DASHBOARD (Shows the final calculated remaining pools)
    print("\n📊 UPDATED BUDGET DASHBOARD STATS:")
    print("-" * 40)
    print(f" - Transport Remaining Budget : ₹{transport_budget:.2f}")
    print(f" - Food Remaining Budget      : ₹{food_budget:.2f}")
    print("-" * 40)

print("\n" + "=" * 60)
print("SmartSpend AI Engine • Execution Finished. Terminating safely...")
print("=" * 60)

# This line forces the program to close out completely and return control to the terminal
sys.exit(0)