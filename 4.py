from random import choice

def login(x):
    fio=x[0].split()
    login=fio[0]+'_'+fio[1][0]+fio[2][0]
    return login


def parol():
    symb='qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    parol=''
    for i in range(10):
        parol+=choice(symb)
    return parol


fin=open('scientist.txt', 'r', encoding='utf-8')
title=fin.readline().strip()
data=[x.strip().split('#') for x in fin]
fin.close()

fout=open('scientist_password.csv', 'w', encoding='utf-8')
fout.write(title+'#login#password\n')
for x in data:
    x=x+[login(x)]+[parol()]
    x='#'.join(x)
    x+='\n'
    fout.write(x)
fout.close()
