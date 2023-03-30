import pandas as pd
import requests

# Define function to geocode a place name using Nominatim API
def geocode_place_name(place_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place_name,
        "format": "jsonv2"
    }
    response = requests.get(url, params=params)
    if response.ok:
        data = response.json()
        if len(data) > 0 and "boundingbox" in data[0]:
            bbox = data[0]["boundingbox"]
            return [bbox[2], bbox[0], bbox[3], bbox[1]]
    return None

# Load the CSV file into a pandas dataframe
df = pd.read_csv("02d-03.csv")

# Apply the geocode_place_name function to the "place" column
df["bbox"] = df["place"].apply(geocode_place_name)

# Write the results to a new CSV file
df.to_csv("02d-03-output.csv", index=False)