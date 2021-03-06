import os
import csv

budget_data_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')
  
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")

    next(csv_reader)

    profLoss = 0
    changeProfLoss = 0
    num_rows = 0
  
    change_Prof_Loss = []
    #actual profits losses
    list1 = []
    #amount of change between months
    list2 = []
    all_months = []
    
    for row in csv_reader:
        print(row)
        list1.append(int(float(row[1])))
        all_months.append(row[0])
    

    list2 = [int(list1[i]-list1[i-1]) for i in range(1,len(list1))]
    max_month = list2.index(max(list2))
    min_month = list2.index(min(list2))
    The_month = all_months[max_month+1]
    The_month2 = all_months[min_month+1]
    
    print('----------------------------')
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {len(list1)} ')
    print(f'Total: ${sum(list1)}')
    print(f'Average Change:  ${(round(sum(list2)/len(list2),2))}') 
    print(f'Greatest Increase in Profits: {The_month}  (${(max(list2))}) ')
    print(f'Greatest Decrease in Profits: {The_month2}  (${(min(list2))}) ')

    with open('PyBank.txt', 'w') as txt:
        txt.writelines(
        '----------------------------'
    'Financial Analysis'
    '----------------------------'
    f'Total Months: {len(list1)} '
    f'Total: ${sum(list1)}'
    f'Average Change:  ${(round(sum(list2)/len(list2),2))}'
    f'Greatest Increase in Profits: {The_month}  (${(max(list2))}) '
    f'Greatest Decrease in Profits: {The_month2}  (${(min(list2))}) '
        )