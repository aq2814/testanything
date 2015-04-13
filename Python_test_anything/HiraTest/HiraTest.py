

'''
Created on 2015. 1. 20.

@author: D2954_IPHONE5S
'''

import urllib

ServiceKey = u'7mhWn2vEf%2FkCnDcdI4K0aFLu2VEKXm%2B4Qf0Aj8a0wf6ACoGbzWnDRQci0w9r6MBO28Eksev6l4cX9MUjS6iM7w%3D%3D'

type1 = 'http://openapi.hira.or.kr/openapi/service/codeInfoService/getSpcHospCodeList?ServiceKey='
type2 = u'http://openapi.hira.or.kr/openapi/service/hospInfoService/getHospBasisList?ServiceKey='

url1 = type1 + ServiceKey
url2 = type2 + ServiceKey
url3 = 'http://www.google.com'
print url2

urllib.urlopen(url2)