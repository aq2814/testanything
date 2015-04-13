# -*- coding: utf-8 -*-
'''
Created on 2015. 3. 4.

@author: D2954_IPHONE5S
'''

import matplotlib.pyplot as plt
import numpy as np
import time
import Image

"""
x = range(100)
y = [i * i for i in x]
print x, y
plt.plot(x, y)
plt.show()"""

file = 'D:\\route_diff\\route_diff_log_bak.txt'

file_open = open(file, 'r')

"""
상암에서 판교
http://map.daum.net/route/carset.json?roadside=ON&callback=jQuery1810403989416314289_1424742554817&carMode=SHORTEST_REALTIME&carOption=NONE&sX=475840&sY=1132843&eX=524055&eY=1084100
상암에서 한남
http://map.daum.net/route/carset.json?roadside=ON&callback=jQuery1810403989416314289_1424742554817&carMode=SHORTEST_REALTIME&carOption=NONE&sX=475840&sY=1132843&eX=501220&eY=1121585

한남에서 낙생육교
http://map.daum.net/route/carset.json?roadside=ON&callback=jQuery1810403989416314289_1424742554817&carMode=SHORTEST_REALTIME&carOption=NONE&sX=501230&sY=1121223&eX=524620&eY=1081175
한남에서 낙생육교 버스
http://apihub.daum.net/route/v2/publictraffic.json?startX=501230&startY=1121223&endX=524620&endY=1081175&inputCoordSystem=WCONGNAMUL&outputCoordSystem=WCONGNAMUL&appkey=93e0a6820c8cbf9d36d74303aac2c838


판교에서 상암
http://map.daum.net/route/carset.json?roadside=ON&callback=jQuery1810403989416314289_1424742554817&carMode=SHORTEST_REALTIME&carOption=NONE&sX=524055&sY=1084100&eX=475840&eY=1132843
한남에서 상암
http://map.daum.net/route/carset.json?roadside=ON&callback=jQuery1810403989416314289_1424742554817&carMode=SHORTEST_REALTIME&carOption=NONE&sX=501220&sY=1121585&eX=475840&eY=1132843

낙생육교에서 한남
http://map.daum.net/route/carset.json?roadside=ON&callback=jQuery1810403989416314289_1424742554817&carMode=SHORTEST_REALTIME&carOption=NONE&sX=524692&sY=1081278&eX=501257&eY=1121383
낙생육교에서 한남 버스
http://apihub.daum.net/route/v2/publictraffic.json?startX=524692&startY=1081278&endX=501257&endY=1121383&inputCoordSystem=WCONGNAMUL&outputCoordSystem=WCONGNAMUL&appkey=93e0a6820c8cbf9d36d74303aac2c838
"""


dt_list = []
time_list1 = []
time_list2 = []
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

q_date = '20150306'
md = q_date[4:]

for line in file_open:
    dt = ''
    route1_time = 0
    route1_dist = 0
    route2_time = 0
    route2_dist = 0
    route3_time = 0
    route3_dist = 0
    route4_time = 0
    route4_dist = 0
    route5_time = 0
    route5_dist = 0
    route6_time = 0
    route6_dist = 0
    route7_time = 0
    route7_dist = 0
    route8_time = 0
    route8_dist = 0
    
    line_list = line.split(',')
    day = line_list[0][4:8]
    dt = line_list[0][8:][0:2] + ':' + line_list[0][8:][2:4]
    
    if day <> md:
        continue
    
    print day, dt
    
    route1_time = int(int(line_list[1]) / 60)
    route1_dist = int(int(line_list[2]) / 1000)
    route2_time = int(int(line_list[3]) / 60)
    route2_dist = int(int(line_list[4]) / 1000)
    route3_time = int(int(line_list[5]) / 60) 
    route3_dist = int(int(line_list[6]) / 1000)
    route4_time = int(int(line_list[7]) / 60) 
    route4_dist = int(int(line_list[8]) / 1000)
    route5_time = int(int(line_list[9]) / 60) 
    route5_dist = int(int(line_list[10]) / 1000)
    route6_time = int(int(line_list[11]) / 60) 
    route6_dist = int(int(line_list[12]) / 1000)
    route7_time = int(int(line_list[13]) / 60) 
    route7_dist = int(int(line_list[14]) / 1000)
    route8_time = int(int(line_list[15]) / 60) 
    route8_dist = int(int(line_list[16]) / 1000)
    
    dt_list.append(dt)
    time_list1.append(route1_time)
    time_list2.append(route2_time)
    

plt.title(q_date + '(' + week[time.strptime(q_date, '%Y%m%d')[6]] + ')')
plt.xticks(range(len(dt_list))[::12], dt_list[::12])
plt.plot(range(len(dt_list)), time_list1, range(len(dt_list)), time_list2)
plt.grid(True)
plt.savefig('c:\\zzz.png')
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
Image.open('c:\\zzz.png').save('c:\\zzz.jpg', 'JPEG')
plt.show()
