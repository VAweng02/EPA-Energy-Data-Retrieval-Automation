import os
import glob
import pandas as pd

def convert_xls_to_csv(input_folder, output_file):
    all_files = glob.glob(os.path.join(input_folder, '**/*.xls'), recursive=True)

    # Initialize an empty DataFrame to store the combined data
    combined_data = pd.DataFrame()

    for file in all_files:
        # Read the XLS file into a DataFrame
        xls_data = pd.read_excel(file)

        # Extract the file name without extension
        file_name = os.path.splitext(os.path.basename(file))[0]

        # Append the DataFrame to the combined data
        combined_data = combined_data.append(xls_data, ignore_index=True)

    # Save the combined data to a CSV file
    combined_data.to_csv(output_file, index=False)

# Specify the input folder containing the nested folders with XLS files
input_folder = './TODO'

# Specify the output file path for the combined CSV data
output_file = 'TODO'

# Convert XLS files to CSV and combine them
convert_xls_to_csv(input_folder, output_file)