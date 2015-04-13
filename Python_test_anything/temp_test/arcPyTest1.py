'''
Created on 2015. 3. 24.

@author: D2954_IPHONE5S
'''

import arcpy

in_f = "d:\\bld_a.gdb\\sensor"

sc = arcpy.SearchCursor(in_f)

for row in sc:
    posx = row.getValue('posx')
    print posx

