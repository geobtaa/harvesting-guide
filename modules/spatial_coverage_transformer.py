import re
import json
import os

# Get the directory of the current script file to find locations.json correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, '..', 'data', 'locations.json')

# Load locations data from JSON file
with open(json_path, 'r') as file:
    locations = json.load(file)

counties_in_pennsylvania = locations['counties_in_pennsylvania']
cities_in_pennsylvania = locations['cities_in_pennsylvania']
state_abbreviations = locations['state_abbreviations']

def transform_spatial_coverage(row, state_abbreviations):
    # Set of terms to ignore (in lowercase for case-insensitive comparison)
    ignore_terms = {
        'united states', 'u.s.', 'usa', 'us', 'conterminous united states', 'conterminous 48 states',
        'lower 48 states', '48 contiguous united states','united states of america', 'united states of america (usa)', 'usda', 'fsa', 'state or equivalent entity',
        'the geographic limits of usa including trust territories', 'county or equivalent entity',
        'usgs world energy region'
    }

    # Replace commas with pipes, then split the string into individual place names
    places = str(row['Creator']).replace(',', '|').split('|')
    transformed_places = []

    for place in places:
        # Check against ignore terms before any cleaning or transformation
        if place.lower().strip() in ignore_terms:
            continue

        # Remove codes like 'PA049 (2022-09-06)' and similar patterns
        cleaned_place = re.sub(r'PA\d+\s*\(.*?\)', '', place).strip()

        # Further remove any standalone 'PA' followed by numbers and potential trailing characters
        cleaned_place = re.sub(r'PA\d+.*?(,|$)', '', cleaned_place).strip()

        # Remove any remaining digits and specific prefixes
        cleaned_place = re.sub(r'\d+', '', cleaned_place).strip()
        cleaned_place = re.sub(r'^(City of|Municipality of)\s+', '', cleaned_place, flags=re.I)

        # Convert state abbreviations to full names
        if cleaned_place in state_abbreviations:
            cleaned_place = state_abbreviations[cleaned_place]

        # Check for 'County' and prepare the name for matching
        if cleaned_place.endswith('County'):
            county_name = cleaned_place.replace('County', '').strip()
            if county_name in counties_in_pennsylvania:
                cleaned_place = f"Pennsylvania--{county_name} County"

        # If not matched as a county, check against cities
        elif cleaned_place in cities_in_pennsylvania:
            cleaned_place = f"Pennsylvania--{cleaned_place}"

        # Sentence case transformation and append if not already present
        cleaned_place = cleaned_place.title()  # Convert to sentence case
        if cleaned_place not in transformed_places:
            transformed_places.append(cleaned_place)

    # Add "Pennsylvania" at the end if it's not already there and relevant
    if 'Pennsylvania' not in transformed_places and any('Pennsylvania--' in s for s in transformed_places):
        transformed_places.append('Pennsylvania')

    return '|'.join(transformed_places)
    
def apply_transformations(df):
    # Assuming state_abbreviations is available in this scope
    global state_abbreviations

    # Pass state_abbreviations as an argument to transform_spatial_coverage
    df['Spatial Coverage'] = df.apply(lambda row: transform_spatial_coverage(row, state_abbreviations), axis=1)
    return df