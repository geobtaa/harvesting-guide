#!/usr/bin/env python
# coding: utf-8

# # Metadata Validation and Clean
# 
# Note: this is the same as the Clean script, but extends the coordinates to 3 decimal points.
# 
# This script will read a CSV of Aardvark metadata to check for required fields and values:
# 1. Resource Class: Checks for a valid entry; if fails -> "Other"
# 2. Access Rights: Checks for a valid entry; if fails -> "Public"
# 3. Date Range: Ensures that the second integer is equal or larger than the first
# 4. Format: Checks if Download is present; if so -> "File"
# 5. Bounding Box: 
#     - Rounds to 3 decimal points
#     - Checks for extremes (180 or 90) and decreases by .001
#     - Checks for points or lines and increases north or east by .0001
#     
# At the end, the script will write the changes to `cleaning_log.csv` and will create a new CSV with the full metadata and cleaned values. The new metadata file will contain a column to indicate if the row was cleaned or not. The column value will excludes rows where the only cleaning action was coordinate rounding.



import pandas as pd
import numpy as np


# Define the acceptable values
resource_class_values = ['Collections','Datasets','Imagery','Maps','Web services','Websites','Other']
access_rights_values = ['Public', 'Restricted']

# Load your CSV file into a pandas DataFrame
# Fill this in with the name of your CSV!!!!
# csv_file_path = 'output_20240408.csv'
# data = pd.read_csv(csv_file_path, low_memory=False)

# Create a DataFrame to store cleaning log
cleaning_log = pd.DataFrame(columns=['ColumnName', 'OriginalValue', 'CleanedValue', 'CleaningAction'])



def clean_resource_class(df):
    """
    Cleans the 'Resource Class' column of the provided DataFrame.
    """
    global cleaning_log
    def clean_row(row):
        resource_class_string = row['Resource Class']
        original = resource_class_string

        if pd.isnull(resource_class_string):
            new_value = 'Datasets'
            cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{ 'ID': row['ID'], 'ColumnName': 'Resource Class', 'OriginalValue': original, 'CleanedValue': new_value, 'CleaningAction': 'Filled empty value with "Datasets"'}])], ignore_index=True)
            return new_value
        else:
            resource_classes = resource_class_string.split('|')
            new_resource_classes = []

            for class_value in resource_classes:
                class_value = class_value.strip()
                if class_value in resource_class_values:
                    new_resource_classes.append(class_value)
                else:
                    new_value = 'Other'  # Default value if no match is found
                    cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{ 'ID': row['ID'], 'ColumnName': 'Resource Class', 'OriginalValue': class_value, 'CleanedValue': new_value, 'CleaningAction': 'Replaced unrecognized value with "Other"'}])], ignore_index=True)
                    new_resource_classes.append(new_value)

            return '|'.join(new_resource_classes)

    df['Resource Class'] = df.apply(clean_row, axis=1)
    return df


def clean_access_rights(df):
    """
    Ensures the 'Access Rights' column exists and cleans it in the provided DataFrame.
    """
    global cleaning_log
    access_rights_values = ['Public', 'Restricted']

    # Ensure 'Access Rights' column exists
    if 'Access Rights' not in df.columns:
        df['Access Rights'] = pd.NA  # Adds the column with missing values

    def clean_row(row):
        x = row['Access Rights']
        original = x

        if pd.isnull(x) or str(x).strip() not in access_rights_values:
            x = 'Public'  # Default to 'Public' if the value is missing or not in the list
            action = 'Filled empty value with "Public"' if pd.isnull(x) else 'Replaced unrecognized value with "Public"'
            cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{ 'ID': row['ID'], 'ColumnName': 'Access Rights', 'OriginalValue': original, 'CleanedValue': x, 'CleaningAction': action}])], ignore_index=True)
        return x

    df['Access Rights'] = df.apply(clean_row, axis=1)
    return df


def clean_date_range(df):
    """
    Cleans the 'Date Range' field in the provided DataFrame.
    """
    global cleaning_log

    def clean_row(row):
        x = row['Date Range']
        original = x
        if pd.isnull(x) or x == '':
            return x  # returns the original value if it's empty or null
        else:
            date_ranges = str(x).split('|')
            for i in range(len(date_ranges)):
                years = date_ranges[i].split('-')

                # Check if both years are either digits or 'Unknown'
                if all(year.isdigit() for year in years):
                    if len(years) == 2 and years[0].isdigit() and years[1].isdigit() and int(years[0]) > int(years[1]):
                        years = sorted(years, key=lambda y: (y.isdigit(), y))
                        date_ranges[i] = '-'.join(years)
                        x = '|'.join(date_ranges)
                        cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{ 
                            'ID': row['ID'], 
                            'ColumnName': 'Date Range', 
                            'OriginalValue': original, 
                            'CleanedValue': x, 
                            'CleaningAction': 'Corrected date order'
                        }])], ignore_index=True)
                else:
                    # Clear the cell if the condition is not met
                    x = ''
                    cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{ 
                        'ID': row['ID'], 
                        'ColumnName': 'Date Range', 
                        'OriginalValue': original, 
                        'CleanedValue': x, 
                        'CleaningAction': 'Cleared non-integer date range'
                    }])], ignore_index=True)
                    break  # Exit the loop as we've cleared the cell

            return x

    df['Date Range'] = df.apply(clean_row, axis=1)
    return df



def clean_format(df):
    """
    Ensures the 'Format' column exists and cleans it in the provided DataFrame.
    """
    global cleaning_log

    # Ensure 'Format' column exists
    if 'Format' not in df.columns:
        df['Format'] = pd.NA  # Adds the column with missing values

    def clean_row(row):
        x = row['Format']
        original = x
        # Fill 'Format' with 'File' if it is missing, regardless of the 'Download' field status
        if pd.isnull(x):
            x = 'File'
            # Log the action
            cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{ 
                'ID': row['ID'], 
                'ColumnName': 'Format', 
                'OriginalValue': (original if pd.notnull(original) else 'Missing'),  # Handling for logging
                'CleanedValue': x, 
                'CleaningAction': 'Filled missing Format value with "File"'
            }])], ignore_index=True)
        return x

    df['Format'] = df.apply(clean_row, axis=1)
    return df

# Function to round decimal places
def round_coordinates(row):
    x = row['Bounding Box']
    original = x
    if pd.isna(x):
        return x
    else:
        pairs = x.split(',')
        new_pairs = []
        for pair in pairs:
            coords = pair.split()
            new_coords = [str(round(float(coord), 3)) for coord in coords]
            new_pair = ' '.join(new_coords)
            global cleaning_log
            if new_pair != pair:
                cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{
                    'ID':row['ID'], 
                    'ColumnName': 'Bounding Box', 
                    'OriginalValue': pair, 
                    'CleanedValue': new_pair, 
                    'CleaningAction': 'Rounded to 3 decimal places'
                }])], ignore_index=True)
            new_pairs.append(new_pair)
        return ','.join(new_pairs)
    
def round_coordinates(df):
    """
    Rounds coordinates in the 'Bounding Box' field.
    """
    global cleaning_log

    def clean_row(row):
        x = row['Bounding Box']
        original = x
        if pd.isna(x):
            return x
        else:
            pairs = x.split(',')
            new_pairs = []
            for pair in pairs:
                coords = pair.split()
                new_coords = [str(round(float(coord), 3)) for coord in coords]
                new_pair = ' '.join(new_coords)
                if new_pair != pair:
                    cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{
                        'ID':row['ID'], 
                        'ColumnName': 'Bounding Box', 
                        'OriginalValue': pair, 
                        'CleanedValue': new_pair, 
                        'CleaningAction': 'Rounded to 3 decimal places'
                    }])], ignore_index=True)
                new_pairs.append(new_pair)
            return ','.join(new_pairs)
    
    df['Bounding Box'] = df.apply(clean_row, axis=1)
    return df

def correct_bounding_box(df):
    """
    Ensures the coordinates are in the correct order for 'Bounding Box' field.
    """
    global cleaning_log

    def clean_row(row):
        bounding_box_str = row['Bounding Box']
        original = bounding_box_str

        try:
            west, south, east, north = map(float, bounding_box_str.split(","))
            
            corrected = False  # Flag to check if correction was made

            # Correct latitude: ensure north >= south
            if north < south:
                north, south = south, north
                corrected = True

            # Correct longitude: ensure east >= west
            if east < west:
                east, west = west, east
                corrected = True

            # Log the correction
            if corrected:
                new_bounding_box_str = f"{west},{south},{east},{north}"
                cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{ 
                    'ID': row['ID'], 
                    'ColumnName': 'Bounding Box', 
                    'OriginalValue': original, 
                    'CleanedValue': new_bounding_box_str, 
                    'CleaningAction': 'Corrected bounding box order'
                }])], ignore_index=True)
                return new_bounding_box_str
            else:
                return bounding_box_str
        
        except Exception as e:
            print(f"Error while correcting bounding box: {e}")
            return bounding_box_str  # Return the original if there's an error

    df['Bounding Box'] = df.apply(clean_row, axis=1)
    return df

def clean_bounding_box(df):
    """
    Adjusts extreme or equal bounding box coordinates.
    """
    global cleaning_log

    def clean_row(row):
        original_coords = str(row['Bounding Box'])
        coords = original_coords.split(',')
        
        if original_coords == '' or original_coords == 'nan' or len(coords) != 4:
            return np.nan

        west, south, east, north = map(float, coords)

        # Adjust if coordinates are at the extremes
        if west in [180.000, -180.000]:
            west = 179.999 if west > 0 else -179.999
        if east in [180.000, -180.000]:
            east = 179.999 if east > 0 else -179.999
        if north == 90.000:
            north = 89.999
        if south == -90.000:
            south = -89.999

        east_modified = False
        north_modified = False

        if west == east:
            east += 0.0001  # Add 0.0001 instead of 0.001
            east_modified = True

        if south == north:
            north += 0.0001  # Add 0.0001 instead of 0.001
            north_modified = True

        # Format coordinates with four decimal places
        new_coords = f"{west:.3f},{south:.3f},{f'{east:.4f}' if east_modified else f'{east:.3f}'},{f'{north:.4f}' if north_modified else f'{north:.3f}'}"

        original_coords_formatted = f"{float(coords[0]):.3f},{float(coords[1]):.3f},{float(coords[2]):.3f},{float(coords[3]):.3f}"
        
        if new_coords != original_coords_formatted:
            cleaning_log = pd.concat([cleaning_log, pd.DataFrame([{
                'ID':row['ID'], 
                'ColumnName': 'Bounding Box', 
                'OriginalValue': row['Bounding Box'],
                'CleanedValue': new_coords, 
                'CleaningAction': 'Corrected line/point to a box or adjusted extreme values'
        }])], ignore_index=True)

    return new_coords

    df['Bounding Box'] = df.apply(clean_row, axis=1)
    return df


def clean_all(df):
    """
    Apply all cleaning functions to the DataFrame.
    """
    df['Resource Class'] = df.apply(clean_resource_class, axis=1)
    df['Access Rights'] = df.apply(clean_access_rights, axis=1)
    df['Date Range'] = df.apply(clean_date_range, axis=1)
    df['Format'] = df.apply(clean_format, axis=1)
    df['Bounding Box'] = df.apply(round_coordinates, axis=1)
    df['Bounding Box'] = df.apply(correct_bounding_box, axis=1)
    df['Bounding Box'] = df.apply(clean_bounding_box, axis=1)
    return df



# ## After cleaning


# Filtering the cleaning_log to exclude rounding-only actions
non_rounding_log = cleaning_log[~cleaning_log['CleaningAction'].str.contains("Rounded to")]

# Create a set with all IDs that have non-rounding cleaning actions
cleaned_ids = set(non_rounding_log['ID'])

cleaned_file_path = "cleaned_" + csv_file_path

# Create a new column 'Cleaned'
data['Cleaned'] = data['ID'].apply(lambda x: 'Yes' if x in cleaned_ids else 'No')

# Write the cleaned data to a CSV file
data.to_csv(cleaned_file_path, index=False)

cleaning_log.to_csv("cleaning_log.csv", index=False)

