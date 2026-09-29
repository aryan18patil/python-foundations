"""
Write a function called vote_calculator() that accepts a single parameter data containing a list of votes, and prints out the candidates (and the number of votes they received) in order
from the most to least votes. The data that stores the votes is a list of tuples, where the first name in the tuple is the name of the voter and the second name is the candidate that they
are voting for.

Unfortunately, some voters attempt to vote more than once -- if they do so, then only the first vote is counted and any other votes are ignored.

Notes:

You can assume that each candidate receives a different number of votes (i.e. there are no ties).
If a candidate does not receive any valid votes, then they are not included in the output (i.e. all candidates receive at least one vote).
"""

def vote_calculator(data):
    candidates = []
    votes = []
    voters = []
    
    for i in range(len(data)):
        if data[i][0] not in voters:
            voters.append(data[i][0])
            
            if data[i][1] in candidates:
                position = candidates.index(data[i][1])
                votes[position] += 1
                
            else:
                candidates.append(data[i][1])
                votes.append(1)
                
    new_list = []
    for i2 in range(len(votes)):
        new_list.append((votes[i2], candidates[i2]))
        
    new_list.sort(reverse=True)
                
    for i3 in range(len(new_list)):
        print(new_list[i3][1], new_list[i3][0])

    print()

source = [('Andrew', 'George'), ('Susan', 'Beverley'), ('Joe', 'Beverley'), ('Ewan', 'Emma'), ('Emma', 'Emma'),('Joe', 'Emma'), ('Bill', 'Beverley')]
vote_calculator(source)

source = [('Andrew', 'George'), ('Andrew', 'George'), ('Andrew', 'Susan')]
vote_calculator(source)
