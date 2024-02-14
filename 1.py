fin=open('scientist.txt', 'r', encoding='utf-8')
title=fin.readline()
data=[x.strip().split('#') for x in fin]
fin.close()
for i in range(len(data)):
    for j in range(len(data)-1):
        if data[j][2]>data[j+1][2]:
            data[j], data[j+1] = data[j+1], data[j]
sc_orig={}
fout=open('scientist_origin.txt', 'w', encoding='utf-8')
fout.write(title)
for x in data:
    if x[1] not in sc_orig:
        sc_orig[x[1]]=x
        s='#'.join(x)+'\n'
        fout.write(s)
fout.close()

flag=False
print('Разработчиками Аллопуринола были такие люди:')
for x in data:
    if x[1]=='Аллопуринол' and flag:
        print(x[0], '-', x[2])
    elif x[1]=='Аллопуринол' and not flag:
        print(x[0], '-', x[2])
        orig_creator=x[0]
        flag=True
print(f'Оригинальный рецепт принадлежит: {orig_creator}')
    


