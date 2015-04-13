# -*- coding: utf-8 -*-
'''
Created on 2015. 3. 5.

@author: D2954_IPHONE5S
'''

file = 'c:\\chain_real.csv'

res = open(file, 'r')

log = 'c:\\chain_log.txt'

logres = open(log, 'w')

dic = {}

ln = 1

for line in res:
    
    if ln % 10000 == 0:
        print ln
    ln += 1

    a = ''
    b = ''
    a, b = line.replace('\n', '').split(',')[0], line.replace('\n', '').split(',')[1]
    chk = 0
    if dic.get(a) == None:
        for key in dic.keys():
            key_list = dic[key]
            #print key_list
            if a in key_list and b in key_list:
                chk = 1
                break
            if a in key_list:
                new_key_list = key_list
                new_key_list.append(b)
                dic[key] = new_key_list
                chk = 1
                break
            if b in key_list:
                new_key_list = key_list
                new_key_list.append(a)
                dic[key] = new_key_list
                chk = 1
                break
        if chk == 0:
            dic[a] = [b]
    else:
        key_append = dic[a]
        key_append.append(b) 
        dic[a] = key_append 
        
print dic

idx = 1

for key in dic.keys():
    logres.write(str(idx) + ',' + str(key) + '\n')
    print idx, key
    for a_val in dic[key]:
        logres.write(str(idx) + ',' + str(a_val) + '\n')
    idx += 1
    
