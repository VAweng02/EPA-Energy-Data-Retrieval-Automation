import requests
import pandas as pd

API_KEY = 'YLClluBS4DJotWC0iBc7HV2b6SxdEcFtSbCu2s5x'

parameters = {
    'api_key': API_KEY,
    'beginDate': '2022-01-01',
    'endDate': '2022-01-02',
    'operatingHoursOnly': True,
    'perPage': 500
}

streamingUrl = "https://api.epa.gov/easey/emissions-mgmt/emissions/apportioned/hourly/by-facility"
streamingResponse = requests.get(streamingUrl, params=parameters)

print("Status code:", streamingResponse.status_code)

if streamingResponse.status_code == 200:
    try:
        streamingResponse_data = streamingResponse.json()
        # Inspect the data structure
        print(streamingResponse_data)
        # Convert the data to a DataFrame
        streamingResponse_df = pd.DataFrame(streamingResponse_data)
        print(streamingResponse_df)
    except Exception as e:
        print("Error occurred while processing the response:", str(e))
else:
    print("Request failed with status code:", streamingResponse.status_code)
