from random import *
fin=open('scientist.txt', 'r', encoding='utf-8')
title=fin.readline().strip()
data=[x.strip().split('#') for x in fin]
fin.close()

a=[int(x) for x in range(1024)]
hash_value=[]
for i in range(len(a)):
    j=[int(x) for x in range(len(a))]
    curr_val=choice(j)
    hash_value.append(a[curr_val])
    a.pop(curr_val)


def hash_str(x, hash_val):
    '''
    Функция создает хэш по ФИО
    :param x: (list) список с данными учёного
    :param hash_val: (list) случайная перестановка чисел от 0 до 1024
    :return: (str) хэш по ФИО
    '''
    hash_str=0
    for i in x:
        hash_str+=hash_value[choice(hash_val)%1024]
    return str(hash_str%2048)


fout=open('scientist _with_hash.csv', 'w', encoding='utf-8')
fout.write(title+'#hash\n')
for x in data:
    x=x+[hash_str(x[0], hash_value)]
    x='#'.join(x)
    x+='\n'
    fout.write(x)
fout.close()
    
    
