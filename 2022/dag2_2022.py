

file1 = open('datadag2_2022.txt', 'r');
Lines = file1.readlines();

data = []
for x in Lines:
    data.append(x.replace("\n", ""))

# print(list(data))
testdata = ['A X', 'A Z', 'B X', 'C Y', 'B X', 'A Z']
# data = testdata

# A = rock              X = lose                (X = rock)
# B = paper             Y = draw                (Y = paper)
# C = scissors          Z = win                 (Z = scissors)
tot_score = 0
# print(data)
for x in data:
    lose = 0; draw = 3;win = 6
    rock = 1;paper = 2;scissors = 3
    
    if x[0] == 'A':
        if x[-1] == 'X':
            tot_score += scissors + lose
        elif x[-1] == 'Y': 
            tot_score += rock + draw
        elif x[-1] == 'Z':
            tot_score += paper + win
    elif x[0] == 'B':
        if x[-1] == 'X':
            tot_score += rock + lose
        elif x[-1] == 'Y': 
            tot_score += paper + draw
        elif x[-1] == 'Z':
            tot_score += scissors + win
    elif x[0] == 'C':
        if x[-1] == 'X':
            tot_score += paper + lose
        elif x[-1] == 'Y': 
            tot_score += scissors + draw
        elif x[-1] == 'Z':
            tot_score += rock + win




print(tot_score)





