import mysql.connector
cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01',
                                      user='root', password='a123456')
    cursor = conn.cursor()
    upd = "update employee set salary = %s where empno =%s"
    data = (60000 ,1011)
    cursor.execute(upd , data)
    conn.commit( )
    print('insert' , cursor.rowcount , "employee")

    sql = "select ename, hiredate, salary from employee where empno =%s"
    cursor.execute(sql,(1011,))
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