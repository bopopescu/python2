print('{0} is {1} years old!'.format('Tom',30))
print('{1} is {0} years old!!'.format('Tom',30))
print('{} is {} years old!'.format('Tom',30))#由左而右給

print('{name} is {age} years old!'.format(name='Tom',age=30))

print('{name} is {age} years old!'.format(name='Tom',age=30))

print('{} is {age} years old!'.format('Tom',age=30))

print('{}, {},{}'.format(123,12354.678,"python1"))
print('{0}, {1},{2}'.format(123,12354.678,"python2"))
print('{0}, {1:.2f},{2}'.format(123,12354.678,"python3"))
print('{}, {:.2f},{}'.format(123,12354.678,"python4"))
print('{}, {:<10.2f},{}'.format(123,12354.678,"python5"))#: 新格式
print('{}, {:10,.2f},{}'.format(123,12354.678,"python6"))

sec =34501

print('{}=秒,{}=時,{}=分,{}=秒'.format(sec,sec//3600,sec%3600//60,sec%60))###


print('{0:d} {1:.2f} {2:s}'.format(123,45.678,'python'))

print('num:{0:8.2f}'.format(45.678))

print('num:{0:<8.2f}'.format(45.678))# :前後不能不空白建
print('num:{0:^8.2f}'.format(45.678))
print('num:{0:*^9.2f}'.format(45.678))

print('num:{0:*>8.2f}'.format(45.678))