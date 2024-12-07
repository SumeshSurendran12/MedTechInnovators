import pandas as pd

def validate_data(df):
    """
    Validates the input data for missing values and invalid department entries.

    Parameters:
        df (pd.DataFrame): A DataFrame containing a 'Department' column.

    Returns:
        pd.DataFrame: A DataFrame with valid entries only.
    """
    try:
        # Check if the 'Department' column exists
        if 'Department' not in df.columns:
            raise ValueError("The DataFrame must contain a 'Department' column.")
        
        # Check for missing values
        if df.isnull().values.any():
            print("Warning: Missing values detected. Rows with missing values will be removed.")
            df = df.dropna()

        # Define valid department values
        valid_departments = ['ER', 'Radiology', 'Surgery', 'Discharge']
        
        # Identify invalid entries
        invalid_entries = df[~df['Department'].isin(valid_departments)]
        if not invalid_entries.empty:
            print(f"Warning: Invalid department entries found:\n{invalid_entries}")
            df = df[df['Department'].isin(valid_departments)]  # Keep only valid rows

        print("Validation completed. Returning cleaned data.")
        return df

    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error