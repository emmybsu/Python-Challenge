import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')
       
# displays header in excel sheet
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_reader)

    #creates blank tally for votes
    votes = 0
    #list of candidates
    candidate_list = []
    #individual candidates
    candidate = []
    cand_dict = {}
    # Count of Total Votes cast
    num_rows = 0
    for row in csv_reader:
       # iterates through candidates.  
       # creates distinct list of candidates and votes.
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
    candidate = list(set(candidate))
    #prints candidate with amount of votes and percentage of votes
    #for i in cand_dict.keys():
    #    print((i),  ((cand_dict[i]/ num_rows)* 100), ('%'), (cand_dict[i]))
    
 
    # sort candidate list
    candidate.sort()  

    print('Election Results')
    print('----------------------------')
    print (f'Total Votes: {num_rows} ')
    print('----------------------------')
    #for key, value in cand_dict.items():
    #    print('{}: {}'.format(key, value))
    for i in cand_dict.keys():
        print(f'{i,(cand_dict[i]),(cand_dict[i]/ num_rows)* 100,2} ')
    print(f'{i,(cand_dict[i]),(cand_dict[i]/ num_rows)* 100,2} ')
    print(candidate)
    #f'%'

    
    # with open('PyPoll.txt', 'w') as txt:
    #     txt.writelines(
    #     '----------------------------'
    # 'Election Results'
    # '----------------------------'
    # f'Total Votes: {num_rows} '
    # '----------------------------'
    # f'{print((i),  ((cand_dict[i]/ num_rows)* 100), (cand_dict[i]))} '
    # f'%'
    #     )
    