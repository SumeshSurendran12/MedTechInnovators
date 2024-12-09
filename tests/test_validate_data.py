import pytest
import pandas as pd
from src.validate_data import validate_data

def test_validate_data_with_valid_departments():
    # Create a DataFrame with all valid departments
    data = {
        'Patient ID': ['P1001', 'P1002', 'P1003'],
        'Department': ['ER', 'Radiology', 'Surgery'],
        'Timestamp': pd.to_datetime(['2023-10-01', '2023-10-02', '2023-10-03'])
    }
    df = pd.DataFrame(data)

    cleaned_df = validate_data(df)

    # With all valid departments and no missing values, the cleaned_df should match the original
    assert len(cleaned_df) == 3, "All valid rows should remain in the DataFrame."
    assert all(dept in ['ER', 'Radiology', 'Surgery', 'Discharge'] for dept in cleaned_df['Department']), \
        "All departments in the cleaned data should be valid."
    pd.testing.assert_frame_equal(cleaned_df, df, check_like=True, 
                                  msg="DataFrame should remain unchanged if data is already valid.")

def test_validate_data_with_invalid_departments():
    # Some departments are invalid and should be removed
    data = {
        'Patient ID': ['P1001', 'P1002', 'P1003'],
        'Department': ['ER', 'Cardiology', 'UnknownDept'],  # 'Cardiology' and 'UnknownDept' are invalid
        'Timestamp': pd.to_datetime(['2023-10-01', '2023-10-02', '2023-10-03'])
    }
    df = pd.DataFrame(data)

    cleaned_df = validate_data(df)

    # Only 'ER' should remain since 'Cardiology' and 'UnknownDept' are invalid
    assert len(cleaned_df) == 1, "Rows with invalid departments should be removed."
    assert cleaned_df['Department'].iloc[0] == 'ER', "The remaining row should have a valid department."

def test_validate_data_with_missing_values():
    # DataFrame contains missing values which should be removed
    data = {
        'Patient ID': ['P1001', 'P1002', None],
        'Department': ['ER', None, 'Surgery'],
        'Timestamp': [pd.Timestamp('2023-10-01'), pd.Timestamp('2023-10-02'), pd.Timestamp('2023-10-03')]
    }
    df = pd.DataFrame(data)

    cleaned_df = validate_data(df)

    # The last two rows have missing values. Only the first row should remain.
    assert len(cleaned_df) == 1, "Rows with missing values should be removed."
    assert cleaned_df['Patient ID'].iloc[0] == 'P1001', "The remaining row should be the first entry."
    assert cleaned_df['Department'].iloc[0] == 'ER', "The remaining row should have a valid department."

def test_validate_data_missing_department_column():
    # DataFrame without 'Department' column should raise a ValueError
    data = {
        'Patient ID': ['P1001', 'P1002', 'P1003'],
        'Timestamp': pd.to_datetime(['2023-10-01', '2023-10-02', '2023-10-03'])
    }
    df = pd.DataFrame(data)

    # Expecting an empty DataFrame returned on error since the function handles exceptions
    cleaned_df = validate_data(df)
    assert cleaned_df.empty, "When 'Department' column is missing, an empty DataFrame should be returned."