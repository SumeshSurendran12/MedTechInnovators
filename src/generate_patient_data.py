import random
import time
import pandas as pd
import os

def generate_patient_data(num_entries=50, valid_departments=None, delay=0, save_to_file=True, file_name="generated_data.csv"):
    """
    Generates mock patient data for a medical facility.

    Parameters:
        num_entries (int): Number of patient entries to generate. Defaults to 50.
        valid_departments (list): List of valid department names. If None, defaults to ['ER', 'Radiology', 'Surgery', 'Discharge'].
        delay (float): Delay in seconds between generating each entry to simulate real-time data generation.
        save_to_file (bool): Whether to save the generated DataFrame to a CSV file in the 'data' directory.
        file_name (str): Name of the CSV file where data will be saved.

    Returns:
        pd.DataFrame: A DataFrame containing the generated patient data.
    """
    if valid_departments is None:
        valid_departments = ['ER', 'Radiology', 'Surgery', 'Discharge']

    data = []
    for _ in range(num_entries):
        patient_id = f'P{random.randint(1000, 9999)}'
        department = random.choice(valid_departments)
        timestamp = pd.Timestamp.now()
        data.append({'Patient ID': patient_id, 'Department': department, 'Timestamp': timestamp})

        if delay > 0:
            time.sleep(delay)

    df = pd.DataFrame(data)

    if save_to_file:
        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", file_name)
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")

    return df

if __name__ == "__main__":
    # Example usage: Generate 50 entries and save them to 'generated_data.csv'
    generate_patient_data()