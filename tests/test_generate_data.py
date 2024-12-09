import pandas as pd
from src.generate_patient_data import generate_patient_data

def test_generate_patient_data():
    # Test generating 50 entries
    df = generate_patient_data(num_entries=50)
    assert len(df) == 50, "Number of generated entries should match 'num_entries'"
    assert 'Patient ID' in df.columns, "DataFrame should contain 'Patient ID' column"
    assert 'Department' in df.columns, "DataFrame should contain 'Department' column"
    assert 'Timestamp' in df.columns, "DataFrame should contain 'Timestamp' column"

    # Verify that all departments match the valid set from generate_patient_data.py
    valid_departments = ['ER', 'Radiology', 'Surgery', 'Discharge']
    assert df['Department'].isin(valid_departments).all(), \
        "All departments should be within the predefined valid list"

def test_real_time_simulation():
    # Test real-time generation with a delay
    df = generate_patient_data(num_entries=5, delay=0.1, save_to_file=False)
    assert len(df) == 5, "Number of generated entries should match 'num_entries'"

    # Check that timestamps are strictly increasing, indicating a delay in generation
    time_diffs = df['Timestamp'].diff().iloc[1:]
    assert (time_diffs > pd.Timedelta(seconds=0)).all(), "Timestamps should increment for real-time simulation"