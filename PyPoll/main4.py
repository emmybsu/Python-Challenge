import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')
       
# displays header in excel sheet
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    
    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')

    next(csv_reader)
    #list of candidates
    #candidate_list = 0
    votes = 0
    #list of candidates
    candidate_list = []
    #individual candidates
    candidate = []
    cand_dict = {}
    # Count of Total Votes cast
    num_rows = 0
    for row in csv_reader:
       # print(row)
        num_rows +=1
        
        if row[2] == 'Khan()' or row[2] == 'Khan':
            candidate.append('Khan')
        else:
            candidate.append(row[2])
        if row[2] == 'Khan()' or row[2] == 'Khan':
            if 'Khan' not in cand_dict:
                cand_dict['Khan'] = 1
            else:
                cand_dict['Khan'] +=1
        
        else:
            if row[2] not in cand_dict:
                cand_dict[row[2]] = 1
            else:
                cand_dict[row[2]] +=1
    print(cand_dict['Khan'])
    print(cand_dict.keys())
    print(cand_dict.values())
    print(cand_dict.items())

    candidate = list(set(candidate))
    def func1(my_diction):
        total = 0
        for i in my_diction:
            total += my_diction[i]
        for j in my_diction:
            my_diction[j] =  '{:.1%}'.format((((float)(my_diction[j])/total)))
        return my_diction
    print(func1(cand_dict))

    print(candidate) 
    candidate.sort()  
    # for x in candidate:
    #     print(x)
    
  

    print('Election Results')
    print('----------------------------')
    print (f'Total Votes: {num_rows} ')
    print('----------------------------')
    for key, value in cand_dict.items():
        print('{}: {}'.format(key, value))
    
