import os
import csv

def find_csv_files(folder_path):
    csv_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root, file))
    return csv_files

def concatenate_csv_files(csv_files, output_file):
    with open(output_file, 'w', newline='') as outfile:
        writer = None
        for csv_file in csv_files:
            with open(csv_file, 'r') as infile:
                reader = csv.reader(infile)
                if writer is None:
                    writer = csv.writer(outfile)
                    writer.writerows(reader)
                else:
                    # Skip the header row for subsequent files
                    next(reader)
                    writer.writerows(reader)



# Specify the folder path containing the nested folders
folder_path = '/path/to/folder'

# Specify the output file path
output_file = '/path/to/output.csv'

# Find all CSV files within the nested folders
csv_files = find_csv_files(folder_path)

# Concatenate the CSV files into the output file
concatenate_csv_files(csv_files, output_file)