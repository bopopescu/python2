# import mysql.connector
#
# cursor = None
# conn = None
# try :
#     conn = mysql.connector.connect(database='db01' , user="root" , password='a123456')
#     cursor = conn.cursor( )
#     sql = 'select ename,hiredate,salary form employee'
#     cursor.execute(sql)
#     emps= cursor.fetchall()
#
#     print(emps)
#
#     for emp in emps:
#         print('name={},hiredate={},salary={}'.format(emp[0],emp[1],emp[2]))
#
#
#     print('total' , cursor.rowcount , 'employee')
#
#
# except mysql.connector.Error as err :
#     print(err)
#
# finally :
#     if conn :
#         conn.close( )
import mysql.connector
cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01',
                                      user='root', password='a123456')
    cursor = conn.cursor()
    sql = "select ename, hiredate, salary from employee"
    cursor.execute(sql)
    emps = cursor.fetchall()
    print(emps)

    for emp in emps:
        print('name={}, hiredate={}, salary={}'.format(emp[0], emp[1], emp[2]))
    print('total', cursor.rowcount, "employee")

except mysql.connector.Error as err:
    print(err)

finally:
    if conn:
        print('database is closed')
        conn.close()