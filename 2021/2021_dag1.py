import math



data = [11, 33, 66, 44, 99, 22, 22, 52, 10];
verandering = [];
verschil = [];
for i in range(len(data)):
    if i == 0:
        print(data[i],' (N/A - no previous measurement)')
        continue
    verschil = data[i] - data[(i-1)];
    if verschil < 0:
        verandering = [*verandering,'increased'];
        print(data[i]," (afgenomen)")
    elif verschil == 0:
        verandering = [*verandering, 'equal']
        print(data[i]," (gelijk gebleven)")
    else:
        verandering = [*verandering,'decreased'];
        print(data[i],' (toegenomen)')


print(verandering)
