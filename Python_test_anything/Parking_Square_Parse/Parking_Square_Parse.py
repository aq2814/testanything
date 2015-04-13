# -*- coding: utf-8 -*-
'''
Created on 2015. 2. 10.

@author: D2954_IPHONE5S
'''

import json
import urllib2

input_file = open('c:\\parking_square.json', 'r')
output_file1 = open('c:\\parking_square_main.csv', 'w')
output_file2 = open('c:\\parking_square_sub1.csv', 'w')
output_file3 = open('c:\\parking_square_sub2.csv', 'w')

output_file1.write('placeid\tlocation_x\tlocation_y\tname\texit_width\texit_height\tparking_width\tparking_height\tstick_height\tparking_class\t\
parking_methode\tparking_inducing\tparking_land\tmemo\tetc\tphone\tzipcode\taddress\taddress_detail\tincline_limit\tprice_original\t\
price_original_time\tprice_max_day\tprice_max_month\toper_time\tnote\trelated_address\tprice_note\torigin\tprice_base\tprice_base_time\tcreated_at\tupdated_at\n')
output_file2.write('placeid\toption_name\toption_value\n')
output_file3.write('photoid\tcreated_at\tupdated_at\tdesc\tarea_id\turl\n')

url = 'http://api3.parkhere.co.kr/areas/external'

page_cnt = json.load(urllib2.urlopen(url))['paginate']['total_pages']

for pagenum in range(page_cnt):
    
    print pagenum
    
    full_url = url + '?page=' + str(pagenum + 1)

    json_load = json.load(urllib2.urlopen(full_url))
    json_areas = json_load['areas']
    cnt = len(json_areas)
    
    for rownum in range(cnt):
        
        id = ''
        location_x = ''
        location_y = ''
        name = ''
        exit_width = ''
        exit_height = ''
        parking_width = ''
        parking_height = ''
        stick_height = ''
        parking_class = ''
        parking_method = ''
        parking_inducing = ''
        parking_land = ''
        memo = ''
        etc = ''
        phone = ''
        zipcode = ''
        address = ''
        address_detail = ''
        incline_limit = ''
        price_original = ''
        price_original_time = ''
        price_max_day = ''
        price_max_month = ''
        oper_time = ''
        note = ''
        related_address = ''
        price_note = ''
        origin = ''
        price_base = ''
        price_base_time = ''
        created_at = ''
        updated_at = ''    
        
        id = str(json_areas[rownum]['area']['id'])
        
        if id == '4101':
            print pagenum + 1
        
        location_x = str(json_areas[rownum]['area']['location_x'] or '')
        location_y = str(json_areas[rownum]['area']['location_y'] or '')
        try:
            name = json_areas[rownum]['area']['name'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949')
        except:
            pass
        exit_width = str(json_areas[rownum]['area']['exit_width'] or '')
        exit_height = str(json_areas[rownum]['area']['exit_height'] or '')
        parking_width = str(json_areas[rownum]['area']['parking_width'] or '')
        parking_height = str(json_areas[rownum]['area']['parking_height'] or '')
        stick_height = str(json_areas[rownum]['area']['stick_height'] or '')
        parking_class = str(json_areas[rownum]['area']['parking_class'] or '')
        parking_method = str(json_areas[rownum]['area']['parking_method'] or '')
        parking_inducing = str(json_areas[rownum]['area']['parking_inducing'] or '')
        parking_land = str(json_areas[rownum]['area']['parking_land'] or '')
        try:
            memo = str(json_areas[rownum]['area']['memo'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949') or '')
        except:
            pass
        try:
            etc = str(json_areas[rownum]['area']['etc'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949') or '')
        except:
            pass
        try:
            phone = str(json_areas[rownum]['area']['phone'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949') or '')
        except:
            pass
        zipcode = str(json_areas[rownum]['area']['zipcode'] or '')
        try:
            address = str(json_areas[rownum]['area']['address'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949') or '')
        except:
            pass
        try:
            address_detail = str(json_areas[rownum]['area']['address_detail'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949') or '')
        except:
            pass
        incline_limit = str(json_areas[rownum]['area']['incline_limit'] or '')
        price_original = str(json_areas[rownum]['area']['price_original'] or '')
        price_original_time = str(json_areas[rownum]['area']['price_original_time'] or '')
        price_max_day = str(json_areas[rownum]['area']['price_max_day'] or '')
        price_max_month = str(json_areas[rownum]['area']['price_max_month'] or '')
        try:
            oper_time = str(json_areas[rownum]['area']['oper_time'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949') or '')
        except:
            pass
        try:
            note = str(json_areas[rownum]['area']['note'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949') or '')
        except:
            pass
        try:
            related_address = str(json_areas[rownum]['area']['related_address'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949') or '')
        except:
            pass
        try:
            price_note = str(json_areas[rownum]['area']['price_note'].replace('\r\n', '').replace('\n', '').replace('\t', '').encode('cp949') or '')
        except:
            pass
        origin = str(json_areas[rownum]['area']['origin'] or '')
        price_base = str(json_areas[rownum]['area']['price_base'] or '')
        price_base_time = str(json_areas[rownum]['area']['price_base_time'] or '')
        created_at = str(json_areas[rownum]['area']['created_at'] or '')
        updated_at = str(json_areas[rownum]['area']['updated_at'] or '')
        
        if id == '4101':
            print pagenum + 1
            print address_detail
            #break
        """
        output_file1.write(id + ',' + location_x + ',' + location_y + ',' + name + ',' + (exit_width) + ',' +
                           exit_height + ',' + parking_width + ',' + parking_height + ',' + stick_height + ',' + 
                           parking_class + ',' + parking_method + ',' + parking_inducing + ',' + parking_land + ',' + 
                           memo + ',' + etc + ',' + phone + ',' + zipcode + ',' + address + ',' + address_detail + ',' + 
                           incline_limit + ',' + str(price_original) + ',' + str(price_original_time) + ',' + price_max_day + ',' + 
                           price_max_month + ',' + oper_time + ',' + note + ',' + related_address + ',' + price_note + ',' + 
                           origin + ',' + str(price_base) + ',' + str(price_base_time) + ',' + created_at + ',' + updated_at + '\n')
        """
        output_file1.write(id + '\t' + location_x + '\t' + location_y + '\t' + name + '\t' + (exit_width) + '\t' +
                           exit_height + '\t' + parking_width + '\t' + parking_height + '\t' + stick_height + '\t' + 
                           parking_class + '\t' + parking_method + '\t' + parking_inducing + '\t' + parking_land + '\t' + 
                           memo + '\t' + etc + '\t' + phone + '\t' + zipcode + '\t' + address + '\t' + address_detail + '\t' + 
                           incline_limit + '\t' + str(price_original) + '\t' + str(price_original_time) + '\t' + price_max_day + '\t' + 
                           price_max_month + '\t' + oper_time + '\t' + note + '\t' + related_address + '\t' + price_note + '\t' + 
                           origin + '\t' + str(price_base) + '\t' + str(price_base_time) + '\t' + created_at + '\t' + updated_at + '\n')

        option_cnt = 0
        option_cnt = len(json_areas[rownum]['area']['options'])
        for rownum_opt in range(option_cnt):
            option_one = json_areas[rownum]['area']['options'][rownum_opt]['option']
            area_id = ''
            option_name = ''
            option_value = ''
            area_id = str(option_one['area_id'])
            option_name = str(option_one['name'])
            option_value = str(option_one['value'])
            output_file2.write(area_id + '\t' + option_name + '\t' + option_value + '\n')
        #print json_areas[rownum]['area']['photos']
        #print json_areas[rownum]['area']['options']
        photo_cnt = 0
        photo_cnt = len(json_areas[rownum]['area']['photos'])
        for rownum_photo in range(photo_cnt):
            photo_one = json_areas[rownum]['area']['photos'][rownum_photo]['photo']
            photo_id = ''
            photo_created_at = ''
            photo_updated_at = ''
            photo_desc = ''
            area_id = ''
            photo_url = ''
            photo_id = str(photo_one['id'])
            photo_created_at = str(photo_one['created_at'])
            photo_updated_at = str(photo_one['updated_at'])
            try:
                photo_desc = str(photo_one['desc'].replace('\r\n', '').replace('\t', '').encode('cp949') or '')
            except:
                pass
            area_id = str(photo_one['area_id'])
            photo_url = str(photo_one['url'])
            output_file3.write(photo_id + '\t' + photo_created_at + '\t' + photo_updated_at + '\t' + photo_desc + '\t' + area_id + '\t' + photo_url + '\n')

output_file1.close()
output_file2.close()
output_file3.close()
    