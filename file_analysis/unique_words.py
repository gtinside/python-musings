"""
File with a function that reads a large text file and counts the number of unique words, 
ignoring case and punctuation

About dataset - Electrical Vehicle Population Data with columns 
VIN (1-10),County,City,State,Postal Code,Model Year,Make,Model,Electric Vehicle Type,
Clean Alternative Fuel Vehicle (CAFV) Eligibility,Electric Range,Base MSRP,Legislative District,
DOL Vehicle ID,Vehicle Location,Electric Utility,2020 Census Tract

Problem 1: Calculate average Electric Range
Problem 2: Top 5 State by Total Electric Vehicles

"""
import tracemalloc
import time
import csv
from collections import defaultdict

csv_file = "Electric_Vehicle_Population_Data.csv"

def solve_by_csv():
    tracemalloc.start()
    start_time = time.time()
    range_data = []
    vehicle_by_state = defaultdict(int)
    with open(csv_file, 'r') as csvFile:
        for line in csv.DictReader(csvFile):
            if line['Electric Range']:
                range_data.append(float(line['Electric Range']))
            
            if line['State']:
                vehicle_by_state[line['State']]+=1
    
    vehicle_by_state = dict(sorted(vehicle_by_state.items(), key=lambda x: x[1], reverse=True)[:5])
    end_time = time.time()
    execution_time = end_time - start_time
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    box_width = 60
    title = "Calculated by csv module"
    # Main Title
    print("╔" + "═" * (box_width - 2) + "╗")
    print("║" + title.center(box_width - 2) + "║")
    print("╠" + "═" * (box_width - 2) + "╣")

    # Data Output Section
    print("║ Average Electric Range :".ljust(40) + str(round(sum(range_data) / len(range_data), 2)).rjust(18) + " ║")
    print("║ Top 5 States by Total Electric Vehicles :".ljust(59) + "║")
    for state, count in vehicle_by_state.items():
        print("║    " + f"{state}: {count}".ljust(54) + "║")

    # Divider
    print("╠" + "═" * (box_width - 2) + "╣")

    # Statistics Section
    print("║" + "Statistics".center(box_width - 2) + "║")
    print("╠" + "═" * (box_width - 2) + "╣")
    print("║ Execution Time :".ljust(40) + f"{execution_time:.2f} seconds".rjust(18) + " ║")
    print("║ Current Memory Usage :".ljust(40) + f"{current_memory/10**6:.2f} MB".rjust(18) + " ║")
    print("║ Peak Memory Usage :".ljust(40) + f"{peak_memory/10**6:.2f} MB".rjust(18) + " ║")

    # Box Footer
    print("╚" + "═" * (box_width - 2) + "╝")



solve_by_csv()
