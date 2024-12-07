import matplotlib.pyplot as plt
import pandas as pd

def visualize_patient_flow(df):
    """
    Visualizes the patient flow in different departments as a bar chart.

    Parameters:
        df (pd.DataFrame): A DataFrame containing a 'Department' column.
    """
    try:
        # Validate if the required column exists
        if 'Department' not in df.columns:
            raise ValueError("The DataFrame must contain a 'Department' column.")

        # Count the number of patients in each department
        flow_count = df['Department'].value_counts()

        # Create the bar chart
        flow_count.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title("Patient Flow Through Departments")
        plt.xlabel("Department")
        plt.ylabel("Number of Patients")
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

# Example data for patient_data
data = {
    'Department': ['Cardiology', 'Neurology', 'Orthopedics', 'Cardiology', 'Neurology', 'Orthopedics', 'Cardiology']
}
patient_data = pd.DataFrame(data)

# Visualize the data
visualize_patient_flow(patient_data)