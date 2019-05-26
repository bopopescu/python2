import mysql.connector
cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01',
                                      user='root', password='a123456')
    cursor = conn.cursor()
    sql="delete from employee where empno = %s"
    cursor.execute(sql,(1011,))
    conn.commit()
    print('insert', cursor.rowcount, "employee")


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