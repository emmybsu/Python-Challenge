import os
import csv

budget_data_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")

    next(csv_reader)

    # i = 0
    # for row in csv_reader:
    #     print(row)
    #     i+=1
    #     if i == 4 : 
    #         break
#print(csv_reader)

    num_rows = 0
    for row in csv_reader:
#        print(row)
        num_rows +=1
#        if i == 4 : 
#            break

    print (num_rows)
