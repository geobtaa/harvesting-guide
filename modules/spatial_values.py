import os
import pandas as pd

def load_csv_data(csv_path):
    """
    Load data from a CSV file into a DataFrame.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the CSV data.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at {csv_path}")

    return pd.read_csv(csv_path)

def match_and_append_values(df, csv_data):
    """
    Match Creator values in the DataFrame to the CSV and append relevant fields.

    Args:
        df (pandas.DataFrame): The input DataFrame with a 'Creator' column.
        csv_data (pandas.DataFrame): DataFrame loaded from the CSV with fields Bounding Box, Geometry, and GeoNames ID.

    Returns:
        pandas.DataFrame: Updated DataFrame with appended fields.
    """
    # Ensure 'Creator' column exists in both DataFrames
    if 'Creator' not in df.columns:
        raise KeyError("The input DataFrame must contain a 'Creator' column.")

    if 'Creator' not in csv_data.columns:
        raise KeyError("The CSV data must contain a 'Creator' column.")

    # Merge DataFrames on the 'Creator' column
    merged_df = pd.merge(df, csv_data, on='Creator', how='left')

    return merged_df

def process_dataframe(input_df_path, output_df_path, csv_path):
    """
    Process an input DataFrame by appending spatial values from a CSV.

    Args:
        input_df_path (str): Path to the input DataFrame file.
        output_df_path (str): Path to save the updated DataFrame.
        csv_path (str): Path to the CSV file.
    """
    # Load input DataFrame
    if not os.path.exists(input_df_path):
        raise FileNotFoundError(f"Input DataFrame file not found at {input_df_path}")

    input_df = pd.read_csv(input_df_path)

    # Load CSV data
    csv_data = load_csv_data(csv_path)

    # Match and append values
    updated_df = match_and_append_values(input_df, csv_data)

    # Save the updated DataFrame
    updated_df.to_csv(output_df_path, index=False)

if __name__ == "__main__":
    # Define file paths
    module_path = os.path.join('..', '..', 'modules', 'spatial_values.py')
    csv_path = os.path.join('..', '..', 'data', 'spatial_counties.csv')
    input_df_path = os.path.join('..', '..', 'data', 'input_dataframe.csv')
    output_df_path = os.path.join('..', '..', 'data', 'output_dataframe.csv')

    # Ensure paths are correct
    print(f"Module Path: {module_path}")
    print(f"CSV Path: {csv_path}")
    print(f"Input DataFrame Path: {input_df_path}")
    print(f"Output DataFrame Path: {output_df_path}")

    # Process the DataFrame
    process_dataframe(input_df_path, output_df_path, csv_path)
