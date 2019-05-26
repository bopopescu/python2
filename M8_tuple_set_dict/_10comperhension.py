x = [i for i in range(1,11)]
print(x)
x = [i*10 for i in range(1,11)]
print(x)

x = {i*10 for i in range(1,11)}#dict
print(x)
x = {i:i*10 for i in range(1,11)}
print(x)

x = (i*10 for i in range(1,11))#tuple
print(x)#<generator object <genexpr> at 0x0000025666337990>
print('-------------------------------')
x = (i*10 for i in range(11))
print(x)
for y in x:
    print(y)

x = [i for i in range(2,31,2)]
print(x)

x = [i for i in range(1,31,2)]
print(x)

x = [i for i in range(1,31) if  i%2==0]
print(x)

x = [i for i in range(1,31) if  i%2==1]
print(x)##########hw 判斷質數

x = [i+1 for i in range(10) if  i%2]
print(x)

x = [i+1 for i in range(10) if  not(i%2)]
print(x)
