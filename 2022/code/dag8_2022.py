file1 = open('2022/data/datadag8_2022.txt','r')
lines = file1.readlines()

data = []
for x in lines:
    data.append(x.replace('\n',''))