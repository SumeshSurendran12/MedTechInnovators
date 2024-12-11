import sys
import os
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.visualize_data import visualize_patient_flow

def test_visualize_patient_flow_with_valid_data():
    """
    Test visualization function with valid data.
    """
    try:
        # Create valid sample data
        sample_data = pd.DataFrame({
            'Patient ID': ['P001', 'P002', 'P003'],
            'Department': ['ER', 'Radiology', 'Surgery'],
            'Timestamp': pd.date_range(start='2023-12-06 12:30:00', periods=3, freq='T')
        })

        # Test visualization function (runs without errors)
        visualize_patient_flow(sample_data, interval=0.1)
        print("Visualization test with valid data passed.")
    except Exception as e:
        assert False, f"Visualization failed with valid data: {e}"

def test_visualize_patient_flow_missing_column():
    """
    Test visualization function with missing 'Department' column.
    """
    try:
        # Create data missing 'Department' column
        invalid_data = pd.DataFrame({
            'Patient ID': ['P001', 'P002', 'P003'],
            'Timestamp': pd.date_range(start='2023-12-06 12:30:00', periods=3, freq='T')
        })

        # Run visualization (should raise an error)
        visualize_patient_flow(invalid_data, interval=0.1)
        assert False, "Visualization did not raise an error for missing 'Department' column."
    except ValueError as e:
        assert str(e) == "The data must contain a 'Department' column", "Unexpected error message for missing 'Department' column."

def test_visualize_patient_flow_empty_data():
    """
    Test visualization function with empty data.
    """
    try:
        # Create empty DataFrame
        empty_data = pd.DataFrame(columns=['Patient ID', 'Department', 'Timestamp'])

        # Run visualization (should not raise an error but display nothing)
        visualize_patient_flow(empty_data, interval=0.1)
        print("Visualization test with empty data passed.")
    except Exception as e:
        assert False, f"Visualization failed with empty data: {e}"

if __name__ == "__main__":
    # Run tests
    test_visualize_patient_flow_with_valid_data()
    test_visualize_patient_flow_missing_column()
    test_visualize_patient_flow_empty_data()
    print("All visualization tests passed.")