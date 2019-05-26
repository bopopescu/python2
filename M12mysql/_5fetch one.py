import mysql.connector
cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01',
                                      user='root', password='a123456')
    cursor = conn.cursor()
    sql = "select ename, hiredate, salary from employee where empno =%s"
    empno= 1001########test 10011
    cursor.execute(sql,(empno,))
    emp = cursor.fetchone()
    if emp is not None:
        print(emp)
        print('name={}, hiredate={}, salary={}'.format(emp [ 0 ] , emp [ 1 ] , emp [ 2 ]))
    else:
        print('no data')

    print('total', cursor.rowcount, "employee")

except mysql.connector.Error as err:
    print(err)

finally:
    if conn :
        print('database is closed')
        conn.close( )