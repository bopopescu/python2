try :
    n1 , n2 = eval ( input ( "enter two numner to divide:" ) )
    div = n1 / n2
    print("{}/{}=".format(n1,n2,num))
except SyntaxError:
    print('need a comma between two number!!!') ##測一個 寫一個
except ZeroDivisionError:
    print("divisor is zero!!")
except:
    print("something wrong!!")
else:
    print('well done')
finally:
    print("always done!")
