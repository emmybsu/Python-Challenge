import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Define the function and have it access the 'election_data' as its sole parameter
# def PyPoll(election_data):
# #     # For readability, it can help to assign your values to variables with descriptive names
#     voterID = int(election_data[0])
#     county = str(election_data[1])
#     candidate = str(election_data[2])
    
       
# displays header in excel sheet
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    
    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')

    next(csv_reader)
    #list of candidates
    #candidate_list = 0
    votes = 0
    #individual candidates
    #candidate = 0
    
    #list of candidates
    candidate_list = []
    #votes = []
    #individual candidates
    candidate = []
    cand_dict = {}
    # Count of Total Votes cast
    num_rows = 0
    for row in csv_reader:
       # print(row)

        num_rows +=1
        #for x in csv_reader:
        #if row[2] not in candidate:
       
        if row[2] == 'Khan()' or row[2] == 'Khan':
            candidate.append('Khan')
        else:
            candidate.append(row[2])

            #candidate.append(x)
        
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

    #for

       
   # print(candidate)
    #candidate.count()

    #x=list(enumerate(candidate))
    #print(x)
    #for count, value in enumerate(candidate):
    candidate = list(set(candidate))

    print(candidate)
        
       #print(count,value)
    #unique_candidate = list(set(row[2])    
     #   print(unique_candidate)
            #print(row[2])
            #unique_candidate = value
            #print(unique_candidate)
        # print name of candidate
        #print(row[2])

    # for row in csv_reader:
    #     candidate_list.append()
    #     print(candidate_list)
    
    #     #all_months.append(row[0])
    # # if num_rows in csv_reader:
    # #     candidate.append()
    # # print(candidate)
        
    #     # print row with 3 items
    # # print(row)
    # #     # iterating across count of rows
    # # candidate = [x for x in row]
    #print (candidate)
    #print(num_rows)
    #print(row[2])
        
        
        




#         candidate_list.append(row[2])
#       #  print(candidate_list)
#         candidate = set(candidate_list)
#  #       print(candidate_list)
#         for group in candidate:
#  #           candidate_list[len(candidate)]
#             #print(group)
#           #print(group[len(group)])
# #            group.append(row[0])
#   #          return votes 
#  #           print(group)
#             votes.append(row[2])
#             votes.sort()
#             print(votes)
#             #all_months.append(row[0])


#     def candidate_list(num_rows):

#         candidate_list = []

#         candidate = set(num_rows)

#         for num_rows in candidate_list:
#             candidate_list.append(num_rows)

#         return candidate_list
#     print(candidate_list(num_rows +1))
# # result: [1, 2, 3, 4, 5]
   
#     for row in csv_reader:
#         candidate_list.append(row[2])
#         candidate.append(row[2])
        
#         # candidate_list = [candidate for list1 in candidate]
#         print(candidate_list)
#         print(candidate)
            

#         for num_rows in csv_reader:
#             candidate_list.append(num_rows)
#         print(num_rows)
        
                
#         print(row)
    
        

    # print('Election Results')
    # print('----------------------------')
    # print (f'Total Votes: {num_rows} ')
    # print('----------------------------')
