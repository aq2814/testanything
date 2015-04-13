# -*- coding: utf-8 -*-s

#from lxml import etree
import xml.etree.ElementTree as ElementTree


targetXML = open('c:\\gcinfoDaum.xml', 'r')

root = ElementTree.fromstringlist(targetXML)

placeid = ''
placename = ''
homepage = ''
hole_count = ''
zone_length =''
zone_area = ''
introduction = ''
tee_off_interval = ''
membership_code = ''
course_url = ''
caddy_fee = ''
weekend_fee = ''
weekdays_fee = ''
address = ''
phone_number = ''
area_code = ''
emblem = ''
course_name = ''
cart_cost = ''
cart_standard = ''

i = 1

for dt in root.iter("field"):

    #print dt.attrib
    if i == 2:
        placeid = dt.text
    elif i == 3:
        homepage = dt.text

    