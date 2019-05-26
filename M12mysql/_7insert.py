import mysql.connector
cursor = None
conn = None
try:
    conn = mysql.connector.connect(database='db01',
                                      user='root', password='a123456')
    cursor = conn.cursor()
    ins ="insert into employee values(%s,%s,%s,%s,%s,%s)"
    data = (1011,"張三李四","2019-05-23",57000,100,'engineer')
    cursor.execute(ins,data)
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