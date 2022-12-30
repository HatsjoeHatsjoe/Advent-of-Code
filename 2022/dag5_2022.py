

file1 = open('datadag5_bewegingen_2022.txt', 'r')
lines = file1.readlines()

data = []
for x in lines:
    data.append(x.replace('\n',''))



rij_1 = ['G' , 'F' , 'V' , 'H' , 'P' , 'S']
rij_2 = ['G','J','F','B','V','D','Z','M']
rij_3 = ['G','M','L','J','N']
rij_4 = ['N','G','Z','V','D','W','P']
rij_5 = ['V','R','C','B']
rij_6 = ['V','R','S','M','P','W','L','Z']
rij_7 = ['T','H','P']
rij_8 = ['Q','R','S','N','C','H','Z','V']
rij_9 = ['F','L','G','P','V','Q','J']

alle_rijen = [rij_1,rij_2,rij_3,rij_4,rij_5,rij_6,rij_7,rij_8,rij_9]

testdata = ['move 6 from 9 to 3', 'move 12 from 2 to 1', 'move 1 from 8 to 2']

# data = testdata
# print(alle_rijen[3])
print(data)

for x in data:
    los = x.split(' ')
    # print(los)
    aantal     = int(los[1])
    print(aantal)
    oude_rij   = int(los[3])
    # print(oude_rij)
    nieuwe_rij = int(los[5])
    # print(nieuwe_rij)
    verplaatsing = alle_rijen[oude_rij-1][-aantal:]
    # print(verplaatsing)
    # verplaatsing.reverse()
    # print(verplaatsing)
    # print(alle_rijen[nieuwe_rij-1])
    alle_rijen[nieuwe_rij-1].extend(verplaatsing)
    # print(alle_rijen[nieuwe_rij-1])
    # print(alle_rijen[oude_rij-1])
    alle_rijen[oude_rij-1] = alle_rijen[oude_rij-1][:-aantal]
    # print(alle_rijen[oude_rij-1])


for i in alle_rijen:
    print(i[-1])




