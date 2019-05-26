# import  mysql.connector
# cursor =None
# conn= None
# try:
#
#     conn = mysql.connector.connect(database='db01' , user="root" , password='a123456')
#     cursor = conn.cursor()
#     sql ='select ename,hiredate,salary form employee'
#     cursor.execute(sql)
#
#     for ename, hiredate,salary in cursor:
#         print("name={}, hiredate={}, salary={}".format(ename,hiredate,salary))
#     print('total',cursor.rowcount,'employee')
#
#
# except mysql.connector.Error as err:
#     print(err)
#
# finally:
#     if conn:
#         conn.close()
#
import mysql.connector
cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01',
                                      user='root', password='a123456')
    cursor = conn.cursor()
    sql = "select ename, hiredate, salary from employee"

    print('total', cursor.rowcount, "employee")
    cursor.execute(sql)
    print('total', cursor.rowcount, "employee")

    for ename, hiredate, salary in cursor:
        print('name={}, hiredate={}, salary={}'.format(ename, hiredate, salary))

except mysql.connector.Error as err:
    print(err)

finally:
    if conn :
        print('database is closed')
        conn.close( )