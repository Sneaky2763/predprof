fin=open('scientist.txt', 'r', encoding='utf-8')
title=fin.readline()
data=[x.strip().split('#') for x in fin]
fin.close()

for i in range(len(data)):
    for j in range(len(data)-1):
        if data[j][2]>data[j+1][2]:
            data[j], data[j+1] = data[j+1], data[j]
for x in data:
    x[2]=x[2].split('-')
    x[2]=''.join(x[2])

while True:
    a=input()
    if a=='эксперимент':
        break
    else:
        flag=True
        a=a.split('.')
        a=a[::-1]
        a=''.join(a)
        L, R = -1, len(data)
        while(L<R-1):
            M=(L+R)//2
            if data[M][2]<a:
                L=M
            elif data[M][2]>a:
                R=M
            elif data[M][2]==a:
                print(f'Ученый {data[M][0]} создал препарат: {data[M][1]} - {data[M][2][-2:]}.{data[M][2][4:6]}.{data[M][2][:4]}')
                flag=False
                break
        if flag:
            print('В этот день ученые отдыхали')
