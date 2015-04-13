import cx_Oracle

connection = cx_Oracle.connect('place', 'placedb', 'PLACE')
cc1 = connection.cursor()

tables = cc1.execute('select table_name from user_tables where rownum <= 10')

for a_table in tables:
    print a_table

connection.close()

