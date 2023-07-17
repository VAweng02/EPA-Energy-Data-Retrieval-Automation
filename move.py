import os
import shutil

def move_files_to_single_folder(source_folder, destination_folder):
    # Iterate through all subfolders and files in the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Get the full path of the current file
            file_path = os.path.join(root, file)
            
            # Move the file to the destination folder
            shutil.move(file_path, destination_folder)

# Specify the source folder containing nested folders and files
source_folder = '/Users/vincentweng/Documents/EPA-Energy-Data-Retrieval-Automation/2020'

# Specify the destination folder where all files will be moved
destination_folder = '/Users/vincentweng/Documents/EPA-Energy-Data-Retrieval-Automation/output'

# Move files to the destination folder



# move_files_to_single_folder(source_folder, destination_folder)




import os
import glob
import pandas as pd

def combine_xls_files(input_folder, output_file):
    all_files = glob.glob(os.path.join(input_folder, '*.xls'))

    # Initialize an empty list to store DataFrames
    data_frames = []

    for file in all_files:
        # Read the XLS file into a DataFrame
        xls_data = pd.read_excel(file)

        # Append the DataFrame to the list
        data_frames.append(xls_data)

    # Concatenate the DataFrames in the list
    combined_data = pd.concat(data_frames, ignore_index=True)

    # Save the combined data to a single Excel file
    combined_data.to_excel(output_file, index=False)

# Specify the input folder containing the .xls files
input_folder = '/Users/vincentweng/Documents/EPA-Energy-Data-Retrieval-Automation/2020'

# Specify the output file path for the combined Excel file
output_file = '/Users/vincentweng/Documents/EPA-Energy-Data-Retrieval-Automation/output_file.xlsx'

# Combine the .xls files into a single Excel file
combine_xls_files(input_folder, output_file)

