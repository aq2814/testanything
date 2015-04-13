# -*- coding: utf-8 -*-
'''
Created on 2014. 10. 24.

@author: D2954_IPHONE5S
'''
import re

def phonenumRemoveZero(phonenum):
    zero_pattern = re.compile('^(0+)([1-9][0-9]+)$')#앞부분의 0을 모두 제거함
    zero_pattern_chk = zero_pattern.match(phonenum)
    try:
        return zero_pattern_chk.groups()[1]
    except:
        return '0'

def phonenumPreChecker(phonenum):#전처리
    phonenum_rem_punct = re.findall('\d', phonenum)#숫자를 제외한 모든 문자/기호 제거함
    phonenum_pre = ''
    for a_num in phonenum_rem_punct:
        phonenum_pre = phonenum_pre + a_num
    #print phonenum_pre[0:1]
    if phonenum_pre.startswith('0'):
        phonenum_pre = phonenumRemoveZero(phonenum_pre)#앞부분의 0을 모두 제거함
    
    #print phonenum_pre
    return phonenum_pre

def phonenumCheckerTypeA(a_region, phonenum_m):#일반적인 시내/시외 전화번호 형태 처리용
        
    phonenum_res = ['','','']
    a_region_res = ''
    phonenum_1st_new = ''
    phonenum_2nd_new = ''
    
    print phonenum_m
    if phonenum_m.startswith('0'):
        #02-0123-4567등과 같이 TypeA에서만 간혹 보이는 형태를 처리하기 위하여 앞쪽의 0을 다시 한 번 처리함
        phonenum_m = phonenumRemoveZero(phonenum_m)
    
    phonenum_len = len(phonenum_m)

    if phonenum_len == 7 and re.match('^[2-9]', phonenum_m): #지역번호를 제외한 나머지가 7~8자리인 경우 맨 앞자리 숫자는 2~9만 가능함
        a_region_res = '0' + a_region
        phonenum_1st_new = phonenum_m[0:3]
        phonenum_2nd_new = phonenum_m[3:]
    elif phonenum_len == 8 and re.match('^[2-9]', phonenum_m):
        a_region_res = '0' + a_region
        phonenum_1st_new = phonenum_m[0:4]
        phonenum_2nd_new = phonenum_m[4:]
    elif phonenum_len == 8 and re.match('^1[3-9]', phonenum_m):#단 지역번호를 제외한 나머지의 첫 번째 숫자가 1로 시작하며 두 번째 숫자가 3~9사이라면 이는 사용 가능함 . 이 경우 지역번호를 사용 안 함(전국공통번호)
        phonenum_1st_new = phonenum_m[0:4]
        phonenum_2nd_new = phonenum_m[4:]
    elif phonenum_len == 3 and re.match('^1[0-2][0-9]', phonenum_m):#지역번호를 제외한 나머지가 세자리이며 1로 시작하는 경우 이는 사용 가능함. 이 경우 지역번호를 사용함(전국공통번호)
        a_region_res = '0' + a_region
        phonenum_1st_new = phonenum_m
        phonenum_2nd_new = ''
    phonenum_res =  [a_region_res, phonenum_1st_new, phonenum_2nd_new]
            
    return phonenum_res

def phonenumCheckerTypeB(a_region, phonenum_m):#030~080시리즈
    
    phonenum_res = ['','','']
    a_region_res = ''
    phonenum_1st_new = ''
    phonenum_2nd_new = ''
    
    phonenum_len = len(phonenum_m)    
    
    if phonenum_len in [7, 8]:#지역번호를 제외한 나머지는 무조건 7~8자리여야함
        idx = int(phonenum_len / 2)
        a_region_res = '0' + a_region
        phonenum_1st_new = phonenum_m[0:idx]
        phonenum_2nd_new = phonenum_m[idx:]
    phonenum_res =  [a_region_res, phonenum_1st_new, phonenum_2nd_new]
    
    return phonenum_res

def phonenumCheckerTypeC(a_region, phonenum_m):#1577-1577등과 같은 생활정보, 부가서비스용 전화번호
    
    phonenum_res = ['','','']
    a_region_res = ''
    phonenum_1st_new = ''
    phonenum_2nd_new = ''
    
    phonenum_len = len(phonenum_m)
    
    if phonenum_len == 6:#지역번호를 제외한 나머지들 중 맨 앞의 두 자리를 제외한 나머지는 6자리여야함
        phonenum_1st_new = phonenum_m[0:2]
        phonenum_2nd_new = phonenum_m[2:]
        phonenum_res =  ['', a_region + phonenum_1st_new, phonenum_2nd_new]
    elif phonenum_len in [7, 8]:#단 이 부분에 핸드폰 번호가 껴 들어오는 경우..짜증나네..
        idx = int(phonenum_len / 2)
        if phonenum_m[0:1] <> '0':
            a_region_res = '0' + a_region
            phonenum_1st_new = phonenum_m[0:idx]
            phonenum_2nd_new = phonenum_m[idx:]
            phonenum_res =  ['0' + a_region, phonenum_1st_new, phonenum_2nd_new]
    
    
    
    return phonenum_res 

def phonenumCheckerTypeD(a_region, phonenum_m):#모바일용 번호
    
    phonenum_res = ['','','']
    a_region_res = ''
    phonenum_1st_new = ''
    phonenum_2nd_new = ''
    
    phonenum_len = len(phonenum_m)
    
    if phonenum_len in [7, 8]:#지역번호를 제외한 나머지는 무조건 7~8자리 사이여야함
        idx = int(phonenum_len / 2)
        if phonenum_m[0:1] <> '0':
            a_region_res = '0' + a_region
            phonenum_1st_new = phonenum_m[0:idx]
            phonenum_2nd_new = phonenum_m[idx:]
    elif phonenum_len == 1:#국번이 112 등과 같이 0을 제외한 휴대폰 국번과 겹치는 경우에 대한 예외 처리
        a_region_res = a_region + phonenum_m
    
    phonenum_res =  [a_region_res, phonenum_1st_new, phonenum_2nd_new]
    
    return phonenum_res

def phonenumCheckerTypeE(a_region, phonenum_m):#시외전화 기간통신사업자용으로써 081-XXX-XXXX 등의 형태임
    
    phonenum_res = ['','','']
    a_region_res = ''
    phonenum_1st_new = ''
    phonenum_2nd_new = ''
    
    phonenum_len = len(phonenum_m)
    
    if phonenum_len in [7, 8]:#지역번호를 제외한 나머지는 무조건 7~8자리 사이여야함
        idx = int(phonenum_len / 2)
        a_region_res = '0' + a_region
        phonenum_1st_new = phonenum_m[0:idx]
        phonenum_2nd_new = phonenum_m[idx:]
    
    phonenum_res =  [a_region_res, phonenum_1st_new, phonenum_2nd_new]
    
    return phonenum_res

def phonenumCheckerTypeF(a_region, phonenum_m):#암 것도 없이 기냥 세 자리의 공공기관 민원 번호만 있는 경우
    
    phonenum_res = ['','','']
    phonenum_1st_new = ''
    phonenum_2nd_new = ''
    
    if phonenum_m == '':    
        phonenum_res =  ['', a_region, '']
    
    return phonenum_res 

def phonenumPostChecker(phonenum_m):
    #02-333-3333, 02-123-4567 등과 같이 의심 되는 패턴들에 대해서 잡아보려 했으나, 좀 더 연구가 필요함...일단 패스~
    pass

def main():
    phoneregion_set = [['2', '31', '32', '33', '41', '42', '43', '44', '51', '52', '53', '54', '55', '61', '62', '63', '64', 'A']
                       ,['30', '50', '60', '70', '80', 'B']
                       ,['13', '14', '15', '16', '18', 'C']
                       ,['10', '11', '16', '17', '18', '19', 'D']
                       ,['81', '82', '83', '84', '85', '86', '87', '88', 'E']
                       ,['100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', 'F']
                       ] 
                       
    phone = '010-9971-6011'
    phonenum_pre = phonenumPreChecker(phone)
    phonenum_new = ['','','']
    
    chk = 0
    flag = ''
    
    for a_region_set in phoneregion_set:
        #print a_region_set
        for a_region in a_region_set:
            if phonenum_pre.startswith(a_region):
                chk = 1
                flag = a_region_set[-1]
                phonenum_pre = phonenum_pre[len(a_region):]
                break
        if chk == 1:
            break
    
    if flag == 'A':
        print 'A'
        phonenum_new = phonenumCheckerTypeA(a_region, phonenum_pre)
    elif flag == 'B':
        print 'B'
        phonenum_new = phonenumCheckerTypeB(a_region, phonenum_pre) 
    elif flag == 'C':
        print 'C'
        phonenum_new = phonenumCheckerTypeC(a_region, phonenum_pre)
    elif flag == 'D':
        print 'D'
        phonenum_new = phonenumCheckerTypeD(a_region, phonenum_pre)
    elif flag == 'E':
        print 'E'
        phonenum_new = phonenumCheckerTypeE(a_region, phonenum_pre)
    elif flag == 'F':
        print 'F'
        phonenum_new = phonenumCheckerTypeF(a_region, phonenum_pre)
    print phonenum_new
    return phonenum_new[0] + '\t' + phonenum_new[1] + '\t' + phonenum_new[2] + '\n' 
    #phonenumMainChecker(phone2)

if __name__ == '__main__':
    main()
        