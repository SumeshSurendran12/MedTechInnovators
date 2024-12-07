import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.generate_data import generate_patient_data

def test_generate_patient_data():
    # Test generating 10 entries
    df = generate_patient_data(num_entries=10)
    assert len(df) == 10, "Number of generated entries should match 'num_entries'"
    assert 'Patient ID' in df.columns, "DataFrame should contain 'Patient ID' column"
    assert 'Department' in df.columns, "DataFrame should contain 'Department' column"
    assert 'Timestamp' in df.columns, "DataFrame should contain 'Timestamp' column"
    assert df['Department'].isin(['ER', 'Radiology', 'Surgery', 'Discharge']).all(), \
        "All departments should be within the predefined valid list"

def test_real_time_simulation():
    # Test real-time generation with delay
    df = generate_patient_data(num_entries=5, delay=0.1)
    assert len(df) == 5, "Number of generated entries should match 'num_entries'"
    assert (df['Timestamp'].diff().iloc[1:] > pd.Timedelta(0)).all(), \
        "Timestamps should increment for real-time simulation"

if __name__ == "__main__":
    test_generate_patient_data()
    test_real_time_simulation()
    print("All tests passed for generate_patient_data.")