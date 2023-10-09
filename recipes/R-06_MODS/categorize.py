## This script will scan determine which rows are parent, child, or standalone

import csv

def classify_row(is_part_of, id, is_part_of_counts):
    # Check for standalone items
    if is_part_of == "06d-01" and is_part_of_counts.get(id, 0) == 0:
        return "standalone"
    # Check for parent items
    elif is_part_of == "06d-01" and is_part_of_counts.get(id, 0) > 0:
        return "parent"
    # Check for child items
    elif "06d-01" in is_part_of and id not in is_part_of:
        return "child"
    else:
        return "unclassified"

def analyze_csv(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Capture header row
        
        # Identify indices of 'Is Part Of' and 'ID' columns
        is_part_of_index = header.index("Is Part Of")
        id_index = header.index("ID")

        # Create a dictionary to count how many times each ID appears in the "Is Part Of" column
        is_part_of_counts = {}
        for row in reader:
            is_part_of_values = row[is_part_of_index].split("|")
            for value in is_part_of_values:
                if value != "06d-01":
                    is_part_of_counts[value] = is_part_of_counts.get(value, 0) + 1

        csvfile.seek(0)  # Reset reader to start of file
        next(reader)  # Skip header row again
        
        # Classify each row
        classifications = []
        for row in reader:
            is_part_of = row[is_part_of_index]
            id = row[id_index]
            classification = classify_row(is_part_of, id, is_part_of_counts)
            classifications.append(row + [classification])
    
    # Write results to a new CSV
    with open('classified_'+file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header + ["Classification"])
        writer.writerows(classifications)

# Execute the function for your file
analyze_csv('children.csv')

