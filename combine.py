import os
import pandas as pd

folders = ['temp']

for folder in folders:

    # Get the current directory
    current_directory = os.getcwd()

    # Set the folder name where your CSV files are located
    folder_name = folder

    # Create the folder path
    folder_path = os.path.join(current_directory, folder_name)

    # Get the list of CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    # Create an empty DataFrame to store the combined data
    combined_data = pd.DataFrame()

    # Iterate over each CSV file
    for file in csv_files:
        # Read the CSV file into a DataFrame
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        
        # Append the DataFrame to the combined_data DataFrame
        # combined_data = combined_data.append(df, ignore_index=True)
        combined_data = pd.concat([combined_data, df], ignore_index=True)

    # Save the combined data to a new CSV file
    combined_data.to_csv(os.path.join(current_directory, 'combined' + folder + '.csv'), index=False)