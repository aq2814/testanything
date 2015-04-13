# -*- coding: utf-8 -*-
'''
Created on 2015. 3. 19.

crong.k@daumkakao.com

@author: D2954_IPHONE5S
'''

import cx_Oracle
import time
import re

connection = cx_Oracle.connect('place','placedb','PLACE')
cc1 = connection.cursor()

def charReplacer(prodname, pattern):
    pattern1 = pattern[0]
    try:
        return pattern1.sub('|', prodname)
    except:
        return ''

def charChecker1(prodname, pattern):
    pattern1 = pattern[0]
    pattern2 = pattern[1]
    pattern3 = pattern[2]
    return pattern3.sub('', pattern2.sub('', pattern1.sub('', prodname)))

def charChecker2(prodname, pattern):
    pattern1 = pattern[0]
    return pattern1.sub('', prodname)

def charChecker3(prodname, pattern):
    pattern1 = pattern[0]
    pattern2 = pattern[1]
    return pattern2.sub('', pattern1.sub('', prodname))
    #return pattern1.sub('', prodname)
    #return pattern2.sub('', prodname)
    
def charChecker4(prodname, pattern_dic):
    for dickey in pattern_dic:
        pattern = r'\d' + dickey[0]
        if re.match(pattern, re.escape(prodname)) > 0:
            return re.sub(pattern, '', prodname)
            #print prodname.decode('mbcs'), prodname_new.decode('mbcs')
        else:
            return prodname
        
def charChecker5(prodname, pattern_dic):
    for dickey in pattern_dic:
        pattern = r' ' + dickey[0] + '$'
        if re.match(pattern, re.escape(prodname)) > 0: 
            return re.sub(pattern, '', prodname)
        else:
            return prodname

def charChecker6(prodname, pattern_dic):
    for dickey in pattern_dic:
        pattern = dickey[0]
        if prodname.find(pattern) >= 0:
            return ''
        else:
            return prodname     

def charChecker7(prodname, pattern):
    pattern1 = pattern[0]
    if re.match(pattern1, re.escape(prodname)) > 0:
        return ''
    else:
        return prodname
    
def charChecker8(prodname):
    if len(unicode(prodname, 'mbcs')) >= 20:
        return ''
    else:
        return prodname


def main():
    logfile = open('c:\\menuname_checker_log.csv', 'w')
    logfile.write('prodname_org,prodname_new\n')
    start_time = time.clock()
    print 'Data reading is started!!!'
    #query1 = "select distinct prodname from (select prodname, status from pl_confirmmenus where rownum <= 10000) where status = 'Y'"
    
    query1 = "select distinct prodname from pl_confirmmenus where status = 'Y' and prodname is not null"
    query2 = "select dickey from zzz_sh_dic_prodname where kind = '1' order by length(dickey) desc"
    query3 = "select dickey from zzz_sh_dic_prodname where kind = '2' order by length(dickey) desc"
    query4 = "select dickey from zzz_sh_dic_prodname where kind = '3' order by length(dickey) desc"
    qres1 = cc1.execute(query1).fetchall()
    qres2 = cc1.execute(query2).fetchall()
    qres3 = cc1.execute(query3).fetchall()
    qres4 = cc1.execute(query4).fetchall()
    
    re_pattern0 = [re.compile(r'[\/+&]')]
    re_pattern1 = [re.compile(r'\([^\(]+\)'), re.compile(r'\[[^\(]+\]'), re.compile(r'{[^\(]+}')]
    re_pattern2 = [re.compile(r'[-\)\(:].+')]
    re_pattern3 = [re.compile(r'\d+[a-zA-Z]+$'), re.compile(r'\d+[!"#$%&()*+,\-./:;<=>?@[\]^_`{|}~]+[\d!"#$%&()*+,\-./:;<=>?@[\]^_`{|}~]+$')]
    re_pattern4 = [re.compile(r'^\d+$')]
    re_pattern5 = [re.compile(r'[ㅏ-ㅣㄱ-ㅎ]')]
    
    print ("Data reading is finished!!! (" + "%d Sec)" % (time.clock() - start_time))
    start_time = time.clock()
    print 'Data checking is started!!!'
    for a_prod1 in qres1:
        a_prodname = a_prod1[0]
        if a_prodname is None:
            print 'aaa'
        res_pre = charReplacer(a_prodname, re_pattern0).split('|')
        for a_prod2 in res_pre:
            res1 = charChecker1(a_prod2, re_pattern1).strip()
            if res1 is None or res1 == '':
                logfile.write(a_prod2 + ',' + '' + '\n')
                continue
            res2 = charChecker2(res1, re_pattern2).strip()
            if res2 is None or res2 == '':
                logfile.write(a_prod2 + ',' + '' + '\n')
                continue
            res3 = charChecker3(res2, re_pattern3).strip()
            if res3 is None or res3 == '':
                logfile.write(a_prod2 + ',' + '' + '\n')
                continue
            res4 = charChecker4(res3, qres2).strip()
            if res4 is None or res4 == '':
                logfile.write(a_prod2 + ',' + '' + '\n')
                continue
            res5 = charChecker5(res4, qres4).strip()
            if res5 is None or res5 == '':
                logfile.write(a_prod2 + ',' + '' + '\n')
                continue
            res6 = charChecker6(res5, qres3).strip()
            if res6 is None or res6 == '':
                logfile.write(a_prod2 + ',' + '' + '\n')
                continue
            res7 = charChecker7(res6, re_pattern4)
            if res7 == '':
                logfile.write(a_prod2 + ',' + '' + '\n')
                continue
            res8 = charChecker7(res7, re_pattern5)
            if res8 == '':
                logfile.write(a_prod2 + ',' + '' + '\n')
                continue            
            res9 = charChecker8(res8)
            if res9 == '':
                logfile.write(a_prod2 + ',' + '' + '\n')
                continue
            logfile.write(a_prod2 + ',' + res9 + '\n')
    print ("Data checking is finished!!! (" + "%d Sec)" % (time.clock() - start_time))
    logfile.close()
    
if __name__ == '__main__':
    main()

