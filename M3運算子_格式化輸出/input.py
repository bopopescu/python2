'''
s = input("input a string")
print(s)
'''
'''
first =  input("input your firstname ")
last =  input("input your lastname")
print(first,last)
'''
'''
first, last = input("input your firstname and lastname:").split()#空白建區分
print(first, last)

salary = input("input your salary")
print ('AnnualSalary={}'.format(int(salary)*12))

salary = int(input("input your salary"))
print ('AnnualSalary={}'.format(salary*12))

salary = eval(input("input your salary"))
print ('AnnualSalary={}'.format(salary*12))

salary = float(input("input your salary"))
print ('AnnualSalary={}'.format(salary*12))
'''

x,y = eval(input("input two numbers: "))
print('total={}'.format(x*y))# , 區分