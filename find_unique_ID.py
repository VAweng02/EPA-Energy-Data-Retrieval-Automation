import pandas as pd

def get_unique_column_values(csv_file, column_name):
    df = pd.read_csv(csv_file)
    unique_values = df[column_name].unique().tolist()
    return unique_values

# Example usage
csv_file = '/Users/vincentweng/Documents/EPA-Energy-Data-Retrieval-Automation/DE_CEMS.csv'
column_name = 'facilityId'

unique_values = get_unique_column_values(csv_file, column_name)
print(unique_values)
print(len(unique_values))