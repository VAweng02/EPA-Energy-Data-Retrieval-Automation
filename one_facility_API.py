import requests
import pandas as pd
import os

API_KEY = 'API KEY'

# Populate year(s) below
years = ['To Fill']

# Insert facility id below
idx = 'To Fill'

# Iterate through each year
for year in years:
    
    # Leap year considerations
    if (year == 2012 or year == 2016 or year == 2020):
        index = [str(year) + '-01-01', str(year) + '-01-15', str(year) + '-01-31', 
                str(year) + '-02-15', str(year) + '-02-29', str(year) + '-03-15', 
                str(year) + '-03-31', str(year) + '-04-15', str(year) + '-04-30', 
                str(year) + '-05-15', str(year) + '-05-31', str(year) + '-06-15', 
                str(year) + '-06-30', str(year) + '-07-15', str(year) + '-07-31', 
                str(year) + '-08-15', str(year) + '-08-31', str(year) + '-09-15', 
                str(year) + '-09-30', str(year) + '-10-15', str(year) + '-10-31', 
                str(year) + '-11-15', str(year) + '-11-30', str(year) + '-12-15', 
                str(year) + '-12-31']
    else:
        index = [str(year) + '-01-01', str(year) + '-01-15', str(year) + '-01-31', 
                str(year) + '-02-15', str(year) + '-02-28', str(year) + '-03-15', 
                str(year) + '-03-31', str(year) + '-04-15', str(year) + '-04-30', 
                str(year) + '-05-15', str(year) + '-05-31', str(year) + '-06-15', 
                str(year) + '-06-30', str(year) + '-07-15', str(year) + '-07-31', 
                str(year) + '-08-15', str(year) + '-08-31', str(year) + '-09-15', 
                str(year) + '-09-30', str(year) + '-10-15', str(year) + '-10-31', 
                str(year) + '-11-15', str(year) + '-11-30', str(year) + '-12-15', 
                str(year) + '-12-31']



    #------------------- API PULL -------------------------------------------------------------------------------------
    i = 0
    while i < 25:

        if (i + 1 == 25):
            break

        parameters = {
            'api_key': API_KEY,
            'beginDate': index[i],
            'facilityId' : idx,
            'endDate': index[i + 1],
            'page' : 1,
            'perPage': 500
        }

        streamingUrl = "https://api.epa.gov/easey/emissions-mgmt/emissions/apportioned/hourly/by-facility"
        streamingResponse = requests.get(streamingUrl, params=parameters)

        print("Status code:", streamingResponse.status_code)

        if streamingResponse.status_code == 200:
            try:
                streamingResponse_data = streamingResponse.json()

                # Inspect the data response(optional)
                print(streamingResponse_data)

                # Convert the data to a df
                streamingResponse_df = pd.DataFrame(streamingResponse_data)

                # Inspect the data structure (optional)
                print(streamingResponse_df)
                
                # Save the data to a CSV file
                name = 'test' + str(i) + '.csv'
                streamingResponse_df.to_csv(name, index=False)
                print("Data saved to test.csv")

            except Exception as e:
                print("Error occurred while processing the response:", str(e))
        else:
            print("Request failed with status code:", streamingResponse.status_code)

        i = i + 1
        
    #-------------------  Removing Duplicates -----------------------------------------------------------------------------------

    # Initialize df
    combined_df = pd.DataFrame()

    # Iterate through the file names
    for i in range(3):
        filename = 'test' + str(i) + '.csv'
        
        try:
            # Read the CSV file into a df
            df = pd.read_csv(filename)
            
            # Append the df to the combined df
            combined_df = pd.concat([combined_df, df], ignore_index=True)
            
            print("File", filename, "appended successfully.")
        except FileNotFoundError:
            print("File", filename, "not found.")
        except Exception as e:
            print("Error occurred while processing file", filename + ":", str(e))

    # Drop duplicate rows from the combined df
    combined_df = combined_df.drop_duplicates()

    # Create a folder to save the combined df
    folder_name = str(idx)     
    os.makedirs(folder_name, exist_ok=True)

    # Save the combined df to a new CSV file
    combined_filename = 'combined' + str(year) + '.csv'
    combined_filepath = os.path.join(folder_name, combined_filename)
    combined_df.to_csv(combined_filepath, index=False)
    print("Combined data saved to", combined_filepath)



    #-------------------  Deleting Duplicate Datasets ---------------------------------------------------------------------------------

    # Iterate through the file names
    for i in range(24):
        filename = 'test' + str(i) + '.csv'
            
        try:
            # Check file existence
            if os.path.exists(filename):
                # Remove the file
                os.remove(filename)
                print("File", filename, "deleted successfully.")
            else:
                print("File", filename, "not found.")
        except Exception as e:
            print("Error occurred while deleting file", filename + ":", str(e))