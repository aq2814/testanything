# -*- coding: utf-8 -*-
import xlrd
import os
import glob
import time
import cx_Oracle

connection = cx_Oracle.connect('place','placedb','PLACE')
cc1 = connection.cursor()
cc2 = connection.cursor()
cc1.execute("truncate table job_temp_cp_mospa")

start_time = time.clock()

root = 'D:\\mopas\\mopas_1412\\'
os.chdir(root)
i = 0

for file in glob.glob('*.xls'):
    print file
    wb = xlrd.open_workbook(root + file)
    sheet_cnt, cnt1 = wb.nsheets, wb.nsheets
    while sheet_cnt >= 1:
        sheet_idx = abs(sheet_cnt - cnt1)
        sh = wb.sheet_by_index(sheet_idx)
        sheet_rownum = sh.nrows
        #print sheet_idx
        #print sheet_rownum

        for row in range(1, sheet_rownum):
            col1 = sh.cell_value(row, 0)
            col2 = sh.cell_value(row, 1)
            col3 = sh.cell_value(row, 2)
            col4 = sh.cell_value(row, 3)
            col5 = sh.cell_value(row, 4)
            col6 = sh.cell_value(row, 5)
            col7 = sh.cell_value(row, 6)
            col8 = sh.cell_value(row, 7)
            cc2.execute("INSERT INTO place.job_temp_cp_mospa VALUES (: seq, :cate1, :cate2, :placename, :addr, :phonenum, :regdttm, :clsdttm)",\
                        {'seq':col1, 'cate1':col2, 'cate2':col3, 'placename':col4, 'addr':col5, 'phonenum':col6,\
                         'regdttm':col7, 'clsdttm':col8})
            i = i + 1
            if i % 1000 == 0:
                connection.commit()
                print i
            #print str(int(col1)) + '\t' + col2 + '\t' + col3 + '\t' + col4 + '\t' + col5 + '\t' + col6 + '\t' + col7 + '\t' + col8

        sheet_cnt = sheet_cnt - 1
connection.commit()
cc1.close()
cc2.close()
