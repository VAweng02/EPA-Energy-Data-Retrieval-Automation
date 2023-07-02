# EPA-Energy-Data-Retrieval-Automation
This automation project simplifies the retrieval of energy data from the U.S. EPA website. It enables the processing of aggregate data with ease and significantly reduces manual extraction from the site.


## Methodology 
My research lab wanted me to accumulate hourly CEMS data from every facility across the United States from 2010 to 2020. Just utilizing the API key on the website directly, there is a limit of about 15 days worth of hourly data per click. That means I would have to run it and wait for the data to be retrieved about 24 times per facility. Given all the facilities in the country, I would have needed to repeat this process over 15,000 times! So I developed this script that increased the speed by more than 7,500%. 


## How To Use
1. Obtain API key from the U.S. EPA website: https://www.epa.gov/power-sector/cam-api-portal#/api-key-signup
2. Insert API key into 'API KEY'
3. Find all the desired facility id(s) and populate the list "facility_ids"
4. Fill in the list "years" with the desired years
5. Run the program and get your data!
