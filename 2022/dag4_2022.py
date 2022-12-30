

file1 = open('datadag4_2022.txt','r')
lines = file1.readlines()

data =[]
for i in lines:
    data.append(i.replace('\n',''))


testdata = ['13-53,17-82', '32-32,32-42', '85-85,8-86', '78-80,79-91', '60-71,59-70', '91-92,4-90']
# data = testdata

kanefficienter = 0

for i in data:
    gesplit = i.split(',')
    # print(gesplit)
    los =[]
    # print('')
    # print('')
    for x in gesplit:
        los.extend(x.split('-'))
        # print(los)
    # print(los)
    elf1 = range(int(los[0]),int(los[1])+1)
    elf2 = range(int(los[2]), int(los[3])+1)
    # print(' elf 1 moet de volgende secties schoonmaken ', elf1)
    # print(' elf 2 moet de volgende secties schoonmaken ', elf2)
    overlap = range(max(elf1[0], elf2[0]), min(elf1[-1], elf2[-1])+1)
    # print('de overlappende secties zijn: ', overlap)
    if len(overlap) > 0:                    # dit gebruiken voor deel 1   == len(elf1) or len(overlap) == len(elf2):
        kanefficienter += 1
    # else:
        # print('')
        # print('het kon niet efficienter')


print('het kon efficienter bij ', kanefficienter, ' elven')



# print(data)


