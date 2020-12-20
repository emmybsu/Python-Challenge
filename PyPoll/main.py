import os
import csv

election_data_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")

    next(csv_reader)

    # i = 0
    # for row in csv_reader:
    #     print(row)
    #     i+=1
    #     if i == 4 : 
    #         break

print(csv_reader)