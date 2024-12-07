import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.validate_data import validate_data
import pandas as pd

def test_validate_data_with_valid_entries():
    # Test with valid entries
    sample_data = pd.DataFrame({
        'Patient ID': ['P001', 'P002', 'P003'],
        'Department': ['ER', 'Radiology', 'Surgery'],
        'Timestamp': ['2023-12-06 12:30:01', '2023-12-06 12:30:02', '2023-12-06 12:30:03']
    })
    cleaned_data = validate_data(sample_data)
    assert len(cleaned_data) == 3, "All valid rows should be retained"
    assert cleaned_data.equals(sample_data), "Valid data should remain unchanged"

def test_validate_data_with_invalid_entries():
    # Test with invalid entries
    sample_data = pd.DataFrame({
        'Patient ID': ['P001', 'P002', 'P003', 'P004'],
        'Department': ['ER', 'InvalidDept', 'Surgery', None],
        'Timestamp': ['2023-12-06 12:30:01', '2023-12-06 12:30:02', '2023-12-06 12:30:03', '2023-12-06 12:30:04']
    })
    cleaned_data = validate_data(sample_data)
    assert len(cleaned_data) == 2, "Rows with invalid or missing departments should be removed"
    assert 'InvalidDept' not in cleaned_data['Department'].values, "Invalid departments should not be in the cleaned data"
    assert not cleaned_data['Department'].isnull().any(), "Cleaned data should not contain missing values"

def test_validate_data_with_missing_column():
    # Test with missing 'Department' column
    sample_data = pd.DataFrame({
        'Patient ID': ['P001', 'P002', 'P003'],
        'Timestamp': ['2023-12-06 12:30:01', '2023-12-06 12:30:02', '2023-12-06 12:30:03']
    })
    try:
        validate_data(sample_data)
        assert False, "An error should be raised if the 'Department' column is missing"
    except ValueError as e:
        assert str(e) == "The DataFrame must contain a 'Department' column", \
            "Error message should indicate missing 'Department' column"

if __name__ == "__main__":
    test_validate_data_with_valid_entries()
    test_validate_data_with_invalid_entries()
    test_validate_data_with_missing_column()
    print("All tests passed for validate_data.")