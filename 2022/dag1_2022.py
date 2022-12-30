import numpy as np


file1 = open('datadag1_2022.txt', 'r');
Lines = file1.readlines();

data =Lines;
teller = 0 ;
# van de getallen integers maken als ze een string zijn.
for x in range(len(data)):
    if data[x] != '\n':
        data[x] = int(data[x])
        teller +=1;
    
testdata = [6669, 6434, 6564, 1032, 1098, 1829, 2608, 7322, 2690, 7061, 1664, 5769, '\n', 6160, 1082, 3958, 5272, 2188, 5618, 3418, 2302, 2926, 3338, 1082, 2024, 4195, 4083, '\n', 3276, 5581, 3421, 3403, 4356, 2989, 1278, 1868, 3630, 4702, 3409, 4887, 2383, '\n', 7104, 7496, 5265, 8078, 8788, 7402, 3601, 2641, 1252, 4994]
# data = testdata;

tot_pers = 0;
beste_guy_1 = 0;
beste_guy_2 = 0;
beste_guy_3 = 0;
for i in range(len(data)):
    
    
    if  isinstance(data[i],int):
        tot_pers += data[i];
        # print(tot_pers)
        if data[i] == data[-1]:
            if beste_guy_1 < tot_pers:
                beste_guy_3 = beste_guy_2
                beste_guy_2 = beste_guy_1
                beste_guy_1 = tot_pers
                print(tot_pers)
                print('deze guy werdt nummer 1')
            elif beste_guy_2 < tot_pers:
                beste_guy_3 = beste_guy_2
                beste_guy_2 = tot_pers
                print(tot_pers)
                print('deze guy werdt nummer 2')
            elif beste_guy_3 < tot_pers:
                beste_guy_3 = tot_pers
                print(tot_pers)
                print('deze guy werdt nummer 3')
    elif data[i] == '\n':
        if beste_guy_1 < tot_pers:
            beste_guy_3 = beste_guy_2
            beste_guy_2 = beste_guy_1
            beste_guy_1 = tot_pers
            print(tot_pers)
            print('deze guy werdt nummer 1')
        elif beste_guy_2 < tot_pers:
            beste_guy_3 = beste_guy_2
            beste_guy_2 = tot_pers
            print(tot_pers)
            print('deze guy werdt nummer 2')
        elif beste_guy_3 < tot_pers:
            beste_guy_3 = tot_pers
            print(tot_pers)
            print('deze guy werdt nummer 3')

        tot_pers = 0

top3 = beste_guy_1+beste_guy_2+beste_guy_3

# print(data[-1])
print(beste_guy_1)
print(beste_guy_2)
print(beste_guy_3)
print(top3)