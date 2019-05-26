'''
def total(x,y):
    z= x+y
    return z
def main ():
    a,b = eval(input("input two numbers to sum up :  "))
    c= total(a,b)
    print('{0}+{1} ={2}'.format(a,b,c))
main()
'''

'''
def factorial1(n):###功能太多 不是用
    result =1
    for  i in range(n,0,-1):
        result *= i
    print("{}! = {}".format((n,result)))
'''
def factorial(n):##0
    result =1 ##2
    for  i in range(n,0,-1):##3
        result *= i##4
    return result##1


def main():##5
   n = eval(input("input  number  :  "))#7

   print("{}! = {}".format(n,factorial(n)))#6
main()#8

