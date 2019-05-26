try:
    n1, n2 = eval(input("enter two numner to divide:  "))
    div = n1/n2
    print("%d/%d=%d"%(n1,n2,div))
except ZeroDivisionError:
    print("division by zero")
except SyntaxError:
    print('comma is missing')
except :
    print('something wrong')
else:
    print('No exeption')
finally:
    print('Must be done')