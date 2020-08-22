#import the data
import os
import csv

#join the path
election_csv= os.path.join ('Resources', 'election_data.csv')

#Variables
Total_votes = 0
percent_votes =0
candidates =[]
candidates_votes= {}
winning_name= ""
winning_votes = 0

#read file
with open (election_csv, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
#skip the header
    header=next(csvreader)
    print (f' Election Results')
    print (f'------------')
    for row in csvreader:
        Total_votes += 1
        #print (Total_votes)
        candidate_name = row [2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidates_votes[candidate_name]=0
            #print (candidates_votes)
        candidates_votes [candidate_name] = candidates_votes [candidate_name]+1
    print (f"Total Votes:  {Total_votes}")
#print (candidates_votes)

#for each candidate add to the list to add number of votes
    for candidate in candidates_votes:
        votes = candidates_votes [candidate]
        print (f'{candidate}: {votes}')
        percent_votes= round(float (votes)/float (Total_votes)*100,2)
        print(percent_votes)
        if votes > winning_votes:
            winning_votes=votes
            winning_name=candidate
    
    
    

    print (f'----------------------------')
    print (f"Winner:   {winning_name}")
#print (winning_votes)
#Write out to:
    output_file = os.path.join('Resources', 'election_data_v2.text')

#write mode
    with open(output_file, 'w') as txtfile:

        txtfile.write(f'Election Results\n')
        txtfile.write(f'-------------\n')
        txtfile.write(f'Total Votes:  {Total_votes}\n')
        txtfile.write(f'-------------\n')
        txtfile.write(f'{candidate}: {votes}\n')
        txtfile.write(f'{percent_votes}\n')
        txtfile.write(f'-------------\n')
        txtfile.write(f'Winner:   {winning_name}\n')




