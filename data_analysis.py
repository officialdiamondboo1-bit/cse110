# ============================================================================
# W06 Project: Life Expectancy Data Analysis
# Author: Godswill Ayang
# ============================================================================

# Step 1: Initialize absolute tracking variables
overall_max_val = -1.0
overall_max_country = ""
overall_max_year = ""

overall_min_val = 999.0
overall_min_country = ""
overall_min_year = ""

# Step 2: Initialize variables for the user's specific year analysis
year_total_expectancy = 0.0
year_count = 0

year_max_val = -1.0
year_max_country = ""

year_min_val = 999.0
year_min_country = ""

# Step 3: Ask the user for their year of interest
interest_year = input("Enter the year of interest (e.g., 1950): ").strip()

# Step 4: Open and parse the verified data rows
with open("life-expectancy.csv", "r", encoding="utf-8") as file:
    header = next(file)  # Skip column headers (Entity,Code,Year,Life expectancy)
    
    for line in file:
        parts = line.strip().split(",")
        
        # Verify row structure matches baseline columns
        if len(parts) < 4:
            continue
            
        country = parts[0].strip()
        code = parts[1].strip()
        year = parts[2].strip()
        
        try:
            expectancy = float(parts[3].strip())
        except ValueError:
            continue
        
        # --- Check for Absolute Overall Maximum / Minimum ---
        if expectancy > overall_max_val:
            overall_max_val = expectancy
            overall_max_country = country
            overall_max_year = year
            
        if expectancy < overall_min_val:
            overall_min_val = expectancy
            overall_min_country = country
            overall_min_year = year
            
        # --- Process Data for the User's Chosen Year ---
        if year == interest_year:
            year_total_expectancy += expectancy
            year_count += 1
            
            # Find the max for this specific year
            if expectancy > year_max_val:
                year_max_val = expectancy
                year_max_country = country
                
            # Find the min for this specific year
            if expectancy < year_min_val:
                year_min_val = expectancy
                year_min_country = country

# Step 5: Output all calculated statistics to the screen
print(f"\nThe overall max life expectancy is: {overall_max_val} from {overall_max_country} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min_val} from {overall_min_country} in {overall_min_year}\n")

# Output specific year data if matches were found in the dataset
if year_count > 0:
    year_avg = year_total_expectancy / year_count
    print(f"For the year {interest_year}:")
    print(f"The average life expectancy across all countries was {year_avg:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max_val}")
    print(f"The min life expectancy was in {year_min_country} with {year_min_val}")
else:
    print(f"No records found for the year {interest_year}.")
