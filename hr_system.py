# Open and read the hr_system.txt file
with open("hr_system.txt") as file:
    for line in file:
        # Clean up any trailing whitespaces or hidden newlines
        clean_line = line.strip()
        
        # Split the line into its individual data parts using space as separator
        parts = clean_line.split(" ")
        
        # Extract variables from parts list
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])
        
        # ENHANCEMENT 1: Calculate paycheck (paid twice a month = 24 periods per year)
        paycheck = salary / 24
        
        # ENHANCEMENT 2: Add a $1000 bonus if the employee is an Engineer
        if job_title == "Engineer":
            paycheck += 1000
            
        # Display the formatted output rounded to 2 decimal places
        print(f"{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}")