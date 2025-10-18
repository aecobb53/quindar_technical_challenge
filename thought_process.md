# Initial understanding

Get csv (telemetry from different locations)
Parse things
    - 
Develop API to:
    - Generate metrics during time window
        - Total data transferred
    - Look for indicators of ground system anomalies
    - Logs information
    - Returns brief summary
Include tests
GitHub Actions workflow (Never done this before but im excited to try)
Define 3 additional datapoints (temperature, etc.) that might come alongside data in csv
    - Create a definition file for each datapoint
        - Name
        - Data Type
        - Nominal Limits / Acceptable Values
    - Create a new csv file (`https://github.com/aecobb53/quindar_technical_challenge`)
        - Include initial data and new fields
        - Update from the Baseline step to read in these values

SEPARATE COMMITS FOR STEPS TO SHOW WORK

# Getting a script working

- Get script working to work out kinks ahead of time and better understand scope

# Getting the FastAPI service stood up

- Get the container working
- Get endpoints responding with simple data
- Get tests working

# Getting a usable version of the service working

- Get the endpoint to run the code from the initial_script.py
- Get the tests working with the correct data (not committed for security)

# After getting the service stood up and things working somewhat I was running low on time

- Get service primary setup working
- Get logging working
- Get actions working

# At this point I had the service working, tests working but I did not set up git hub actions correctly
