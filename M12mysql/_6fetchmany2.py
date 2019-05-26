import mysql.connector
cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01',
                                      user='root', password='a123456')
    cursor = conn.cursor()
    sql = "select ename, hiredate, salary from employee where deptno =%(deptno)s and title =%(title)s"
    deptno =100
    title = "engineer"
    cursor.execute(sql,{"deptno":deptno,"title":title})

    for ename, hiredate, salary in cursor:
        print('name={}, hiredate={}, salary={}'.format(ename, hiredate, salary))
    print('total', cursor.rowcount, "employee")

except mysql.connector.Error as err:
    print(err)

finally:
    if conn :
        print('database is closed')
        conn.close( )