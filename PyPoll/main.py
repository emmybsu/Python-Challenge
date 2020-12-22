import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Define the function and have it access the 'election_data' as its sole parameter
def PyPoll(election_data):
    # For readability, it can help to assign your values to variables with descriptive names
    voterID = int(election_data[0])
    county = str(election_data[1])
    candidate = str(election_data[2])

    
    
# displays header in excel sheet
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")

    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')

    next(csv_reader)

    # Count of Total Votes cast
    num_rows = 0
    for row in csv_reader:
        num_rows +=1
    

        

    print('Election Results')
    print('----------------------------')
    print (f'Total Votes: {num_rows} ')

# candidate = list(set(candidate))
# print(candidate)


    


