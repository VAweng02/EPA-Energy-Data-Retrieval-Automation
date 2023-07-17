import requests
import pandas as pd
import os


API_KEYS = ['sB93MbrJg93yx0Nrla0xYb4ar46BbiKrlRYXjlZq',
            'CXIh5JupiC4anbN9bfYf2EjkzDuE88sUCuNWBjj7',
            'D4w6dYI1AGxF02TlyEquSfqTJ14WtUs1su4f8veW']


# Populate facility id(s) below
total_facility_ids = [10030, 7318, 593, 591, 7962, 594, 7153, 599, 52193]

partition_idx = 0

for API_KEY in API_KEYS:

    if (partition_idx+3 <= len(total_facility_ids)):
        facility_ids = total_facility_ids[partition_idx:partition_idx+3]
    
    else:
        facility_ids = total_facility_ids[partition_idx:]

    # Exit loop if status code is 429 (optional)
    leave = False 

    for id in facility_ids:

        # Populate year(s) below
        years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

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
                    'facilityId' : id,
                    'endDate': index[i+1],
                    'page' : 1,
                    'perPage': 500
                }

                streamingUrl = "https://api.epa.gov/easey/emissions-mgmt/emissions/apportioned/hourly"
                streamingResponse = requests.get(streamingUrl, params=parameters)

                print("Status code:", streamingResponse.status_code)

                # leave=true when status code is 429 (API key runs out)
                if streamingResponse.status_code == 429:
                    leave = True
                    break

                if streamingResponse.status_code == 200:
                    try:
                        streamingResponse_data = streamingResponse.json()
                        # Inspect the data structure
                        print(streamingResponse_data)
                        # Convert the data to a DataFrame
                        streamingResponse_df = pd.DataFrame(streamingResponse_data)
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
                
            if (leave == True):
                break


            
            #-------------------  Removing Duplicates -----------------------------------------------------------------------------------

            # Initialize an empty DataFrame
            combined_df = pd.DataFrame()

            # Iterate through the file names
            for i in range(24):
                filename = 'test' + str(i) + '.csv'
                
                try:
                    # Read the CSV file into a DataFrame
                    df = pd.read_csv(filename)
                    
                    # Append the DataFrame to the combined DataFrame
                    # combined_df = combined_df.append(df, ignore_index=True)
                    combined_df = pd.concat([combined_df, df], ignore_index=True)
                    
                    print("File", filename, "appended successfully.")
                except FileNotFoundError:
                    print("File", filename, "not found.")
                except Exception as e:
                    print("Error occurred while processing file", filename + ":", str(e))

            # Drop duplicate rows from the combined DataFrame
            combined_df = combined_df.drop_duplicates()

            # Create a folder to save the combined DataFrame
            folder_name = str(id)
            os.makedirs(folder_name, exist_ok=True)

            # Save the combined DataFrame to a new CSV file
            combined_filename = 'combined' + str(year) + '.csv'
            combined_filepath = os.path.join(folder_name, combined_filename)
            combined_df.to_csv(combined_filepath, index=False)
            print("Combined data saved to", combined_filepath)



            #-------------------  Deleting Duplicate Datasets ---------------------------------------------------------------------------------

            # Iterate through the file names
            for i in range(24):
                filename = 'test' + str(i) + '.csv'
                    
                try:
                    # Check if the file exists
                    if os.path.exists(filename):
                        # Delete the file
                        os.remove(filename)
                        print("File", filename, "deleted successfully.")
                    else:
                        print("File", filename, "not found.")
                except Exception as e:
                    print("Error occurred while deleting file", filename + ":", str(e))
        

        if (leave == True):
                break

    partition_idx += 3