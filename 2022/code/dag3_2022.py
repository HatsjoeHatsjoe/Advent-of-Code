
file1 = open('datadag3_2022.txt','r')
lines = file1.readlines()

data = []
for x in lines:
    data.append(x.replace('\n',''))

testdata = ['jLnFTjhwFTLFDGDDvLgvDssBJBbVRNZJPPJBGzBNRVJNRB', 'QWmffSmMZCfWrmHlCflQWfSNBpVBNbPSbbJNppcVVzzpcp']
# data = testdata
value = 0;
for x in range(0,len(data),3):
    # n = len(x)
    # str1 = x[0:n//2]
    # str2 = x[n//2:]
    commen = set(data[x])&set(data[(x + 1)])&set(data[(x + 2)])
    print('the commen letter is ',commen)
    # print(str1)
    # print(str2)
    n = [ord(z) - 96 for z in commen]
    for i in n:
        n = int(i)
    if n < 0:
        n += 58
    print(n)
    value += n

print(value)





# print(data)