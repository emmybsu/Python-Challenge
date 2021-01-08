import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')
       
# displays header in excel sheet
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    
    csv_header = next(csv_reader)
    #print(f'CSV Header: {csv_header}')

    #list of candidates
    votes = 0
    #list of candidates
    candidate_list = []
    #individual candidates
    candidate = []
    cand_dict = {}
    # Count of Total Votes cast
    num_rows = 0
    for row in csv_reader:
  
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

    #print to terminal
    candidate = list(set(candidate))
    print('Election Results')
    print('----------------------------')
    print (f'Total Votes: {num_rows} ')
    print('----------------------------')
    #calculate votes for each candidate in terminal

    for i in cand_dict.keys():
        print((i),  (str(round((cand_dict[i]/ num_rows)* 100, 3)) + '%'), (cand_dict[i]))
            
    

    #print(candidate) 
    candidate.sort() 

    winner = ''
    max_vote = 0
    for i in cand_dict.keys():
        if cand_dict[i] > max_vote:
            winner = i
            max_vote = cand_dict[i]
    print('----------------------------')
    print(winner)
    print('----------------------------')
        
#print to text file
    filename = open('PyPoll.txt', 'w+')    
    filename.write('Election Results')
    filename.write('\n')
    filename.write('----------------------------')
    filename.write('\n')
    filename.write('Total Votes: ' + str(num_rows))
 
    filename.write('\n')
    filename.write('----------------------------')
    filename.write('\n')
    #calculate votes for each candidate in text file
    for i in cand_dict.keys():
        filename.write(((i) +": " + (str(round((cand_dict[i]/ num_rows)* 100, 3)) + '%') + " " + '('+ str(cand_dict[i]))+  ')' + ' \n' )
    filename.write('----------------------------')
    filename.write('\n')
    filename.write('Winner: ' + str(winner))
    filename.write('\n')
    filename.write('----------------------------')
    

