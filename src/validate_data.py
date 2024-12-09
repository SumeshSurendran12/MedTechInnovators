import pandas as pd

def validate_data(df):
    """
    Validates the input DataFrame for completeness and department values.

    Steps performed:
    1. Checks if the 'Department' column exists; if not, raises a ValueError.
    2. Removes rows containing missing values.
    3. Removes rows containing departments not in the valid list: ['ER', 'Radiology', 'Surgery', 'Discharge'].

    Parameters:
        df (pd.DataFrame): The DataFrame to validate.

    Returns:
        pd.DataFrame: A cleaned and validated DataFrame.

    On-screen:
        Prints warnings if missing values or invalid departments are found.
        Prints a completion message when validation is done.
    """
    try:
        if 'Department' not in df.columns:
            raise ValueError("The DataFrame must contain a 'Department' column.")

        # Check and remove missing values
        if df.isnull().values.any():
            print("Warning: Missing values detected. Rows with missing values will be removed.")
            df = df.dropna()
        else:
            print("No missing values found.")

        # Define valid departments and remove invalid entries
        valid_departments = ['ER', 'Radiology', 'Surgery', 'Discharge']
        invalid_entries = df[~df['Department'].isin(valid_departments)]
        if not invalid_entries.empty:
            print(f"Warning: Invalid department entries found:\n{invalid_entries}")
            df = df[df['Department'].isin(valid_departments)]
        else:
            print("No invalid department entries found.")

        print("Validation completed. Returning cleaned data.")
        return df

    except Exception as e:
        print(f"Error during validation: {e}")
        return pd.DataFrame()

{
  "configurations": [
    {
      "type": "debugpy",
      "request": "launch",
      "name": "Launch generate_patient_data",
      "program": "${workspaceFolder}/src/generate_patient_data.py"
    },
    {
      "type": "debugpy",
      "request": "launch",
      "name": "Launch validate_data",
      "program": "${workspaceFolder}/src/validate_data.py"
    },
    {
      "type": "debugpy",
      "request": "launch",
      "name": "Launch visualize_patient_flow",
      "program": "${workspaceFolder}/src/visualize_patient_flow.py"
    }
  ]
}