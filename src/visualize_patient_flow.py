import matplotlib.pyplot as plt
import pandas as pd

def visualize_patient_flow(df):
    """
    Visualizes the patient flow in different departments as a bar chart.
    """
    try:
        if 'Department' not in df.columns:
            raise ValueError("The DataFrame must contain a 'Department' column.")

        flow_count = df['Department'].value_counts()
        flow_count.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title("Patient Flow Through Departments")
        plt.xlabel("Department")
        plt.ylabel("Number of Patients")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example data
    data = {
        'Department': ['ER', 'ER', 'Radiology', 'Surgery', 'ER', 'Radiology', 'Discharge', 'Surgery', 'Surgery']
    }
    df = pd.DataFrame(data)

    # Call the visualization function
    visualize_patient_flow(df)