fin=open('scientist.txt', 'r', encoding='utf-8')
title=fin.readline()
data=[x.strip().split('#') for x in fin]
fin.close()
for i in range(len(data)):
    for j in range(len(data)-1):
        if data[j][2]>data[j+1][2]:
            data[j], data[j+1] = data[j+1], data[j]
cnt=0
for x in data:
    print(x[0], '-', x[1])
    cnt+=1
    if cnt==5:
        break
