
import shapefile
import shapely
import cx_Oracle
import sdo
from sdo import Geometry as SdoGeometry
from shapely.geometry import asShape
import time


cx = cx_Oracle.makedsn('10.12.225.12',1521,'spatialM')
connection = cx_Oracle.connect('place','place',cx)
cc1 = connection.cursor()

start_time = time.clock()

diminfo = "MDSYS.SDO_DIM_ARRAY(MDSYS.SDO_DIM_ELEMENT('D',-1800000,1800000,5E-9),MDSYS.SDO_DIM_ELEMENT('D',-1800000,-1800000,5E-9))"
#sql = ("select shape from zzz_sh_rtree_a")
sql = ("select objectid, \
sdo_geom.sdo_max_mbr_ordinate(shape, " + diminfo + ", 1),\
sdo_geom.sdo_max_mbr_ordinate(shape, " + diminfo + ", 2),\
sdo_geom.sdo_min_mbr_ordinate(shape, " + diminfo + ", 1),\
sdo_geom.sdo_min_mbr_ordinate(shape, " + diminfo + ", 2)\
 from ndm.danjiall_a where objectid <= 10000")
res = cc1.execute(sql)
obj = res.fetchall()

print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))


print 'Reading Sdo Object Completed!!'

obj_all = []

start_time = time.clock()

for a_obj in obj:
    #obj_all.append(list(asShape(SdoGeometry(a_obj[1])).bounds))
    #print a_obj[1].SDO_ORDINATES
    obj_all.append(a_obj[1])

print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))

#obj_all = [list(asShape(SdoGeometry(a_obj[1])).bounds) for a_obj in obj]

print 'Boundary Creation Completed!!'

"""
polygons_sf = shapefile.Reader("C:\\pyspatial_test\MAPO_RTREE_TEST.shp")
polygon_shapes = polygons_sf.shapes()
"""
"""
start_time = time.clock()

from rtree import index
idx = index.Index()
cnt = -1
for q in obj_all:
    
    cnt +=1
    print cnt
    idx.insert(cnt, q)

print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))



p = SdoGeometry(obj)
print [q for q in asShape(p).bounds]

#print obj[0][0].SDO_ORDINATES
#print obj.SDO_ORDINATES


###Load the shapefile of polygons and convert it to shapely polygon objects

start_time = time.clock()

polygons_sf = shapefile.Reader("C:\\pyspatial_test\MAPO_RTREE_TEST.shp")
polygon_shapes = polygons_sf.shapes()
polygon_points = [q.points for q in polygon_shapes]
from shapely.geometry import Polygon
polygons = [Polygon(q) for q in polygon_points]
#print polygons[0]

print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))

###Load the shapefile of points and convert it to shapely point objects

points_sf = shapefile.Reader("C:\\pyspatial_test\Point.shp")
point_shapes = points_sf.shapes()
from shapely.geometry import Point
point_coords= [q.points[0] for q in point_shapes]
points = [Point(q.points[0]) for q in point_shapes]

###Build a spatial index based on the bounding boxes of the polygons

###print polygon_shapes[0].bbox #MBR 

start_time = time.clock()

from rtree import index
idx = index.Index()
count = -1
for q in polygon_shapes:
    count +=1
    idx.insert(count, q.bbox)

print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))

###Assign one or more matching polygons to each point

matches = []
for i in range(len(points)): #Iterate through each point
    temp= None
    print "Point ", i, points_sf.records()[i]
    #Iterate only through the bounding boxes which contain the point
    for j in idx.intersection( point_coords[i]):
        #Verify that point is within the polygon itself not just the bounding box
        if points[i].within(polygons[j]):
            print "Match found! ", j, points_sf.records()[i], polygons_sf.records()[j] 
            temp=j
            break
    matches.append(temp) #Either the first match found, or None for no matches
"""
