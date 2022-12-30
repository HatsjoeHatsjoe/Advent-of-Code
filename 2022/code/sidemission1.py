
import re


def repfree(s):
    if re.search(r'^.*(.).*\1.*$', s):
        print("False")
    else:
        print("True")
        
def find_dup_char(input):
    x=[]
    for i in input:
        if i not in x and input.count(i)>1:
            x.append(i)
    print(" ".join(x))
        

file1 = open('sidemission.txt','r')
line = file1.readline()
n = 16
data = line
losse = [(data[i:i+n]) for i in range(0, len(data), n)]

testdata = ['wDzZAhkuGAMoRSAZ', 'aCPAbIm0Az6eoAgA', 'LPYSBsPYQBwnYmBy', 'FSOBu9NaBSPykB9B']
data = testdata
data = losse
for i in data:
    if len(set(i)) == len(i):
        print(i)
        print('no duplicate')

print(len(line)/16)    


# print(data)