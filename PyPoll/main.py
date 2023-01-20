import csv
import os
candidate_dictionary = dict()
number_of_votes = 0
winner_name = ""
candidate = ""

election_file =  os.path.join('Resources', 'election_data.csv')   
with open(election_file, mode='r') as data_file:

    csvFile = csv.reader(data_file)
    next(csvFile) 
    for line in csvFile:
        candidate = line[2]     
        if candidate not in candidate_dictionary:
            candidate_dictionary.update({candidate: 1})
        else:
            candidate_dictionary[candidate] = candidate_dictionary[candidate] + 1

winner = max(candidate_dictionary, key=candidate_dictionary.get)
number_of_votes = sum(candidate_dictionary.values())

print()
print("Election Results")
print("-------------------------------------------------------")
print("Total votes: {}".format(number_of_votes))
print("-------------------------------------------------------")
for candidate, votes in candidate_dictionary.items():
    print("{}: {}% ({})".format(candidate, round((100*votes/number_of_votes), 3), votes))
print("-------------------------------------------------------")
print("The winner: {}".format(winner))
print("-------------------------------------------------------")