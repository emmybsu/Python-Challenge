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
    profLoss = 0
    changeProfLoss = 0
    num_rows = 0
    for row in csv_reader:
        profLoss +=int(row[1])
        
  #      if num_rows == 4 : 
 #          break
        
        if num_rows != 0:
           changeProfLoss += int(row[1]) - prevProf

        prevProf = int(row[1])

        num_rows +=1

    
   
    print (num_rows)

    print('Financial Analysis')
    print('----------------------------')
    print (f'Total Months: {num_rows} ')

    # Count of Total Votes cast
 #  num_rows = 0
 # for row in csv_reader:
 #    num_rows +=1
    
    print(row)
    print(profLoss)
    print(profLoss/ num_rows)
    print(changeProfLoss/ num_rows)
 #   print(changeProfLoss/ )
