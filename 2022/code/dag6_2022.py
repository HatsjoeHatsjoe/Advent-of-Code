
file1 = open('datadag6_2022.txt', 'r')
line = file1.readline()


testdata = 'vldvlvvhwhttcsttpntnvvqpqpdhmlddwhwcwnwmwfwppdrrhllcw'
# line = testdata

# print(len(line))
# print(line)

for x in range(len(line)):
    check = set(line[x:x+14])
    echte = line[x:x+14]
    # print(check)
    # print(echte)
    if len(check) == len(echte):
        print(x+14)
        break
    
    