import random
import time
import pandas as pd
import os

def generate_patient_data(num_entries=50, valid_departments=None, delay=0, save_to_file=True, file_name="generated_data.csv"):
    """
    Generates mock patient data for a medical facility.

    Parameters:
        num_entries (int): Number of patient entries to generate.
        valid_departments (list): Valid department names. Defaults to standard departments.
        delay (float): Delay between generating each entry to simulate real-time behavior.
        save_to_file (bool): Whether to save the generated data to a file.
        file_name (str): Name of the output file.

    Returns:
        pd.DataFrame: A DataFrame containing generated patient data.
    """
    if valid_departments is None:
        valid_departments = ['ER', 'Radiology', 'Surgery', 'Discharge', 'Cardiology', 'Oncology', 'Pediatrics']

    data = []
    for _ in range(num_entries):
        patient_id = f'P{random.randint(1000, 9999)}'
        department = random.choice(valid_departments)
        timestamp = pd.Timestamp.now()
        data.append({'Patient ID': patient_id, 'Department': department, 'Timestamp': timestamp})

        if delay > 0:
            time.sleep(delay)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to file if requested
    if save_to_file:
        os.makedirs("data", exist_ok=True)  # Create 'data' folder if it doesn't exist
        file_path = os.path.join("data", file_name)
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")

    return df

# Example Usage
if __name__ == "__main__":
    patient_data = generate_patient_data(num_entries=50, valid_departments=['ER', 'Radiology', 'Surgery', 'Discharge', 'Cardiology', 'Oncology', 'Pediatrics'], delay=0.5, save_to_file=True)
    print(patient_data)