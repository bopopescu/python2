##### 值均為字串
dict1 = {'name': 'tom','age':25, 'mobile ': '0934111222'}
#        {字串: 說明}
print(dict1)
print(tuple(dict1))#print(tuple(dict1))

print(type(dict1))
print(dict1['name'])#tom
print(dict1.get('name'))

for key in dict1:
    print("{}:{}".format(key,dict1[key]))#取值

##P135
print(dict1.keys())
print(list(dict1.keys()))
print(tuple(dict1.keys()))

print(dict1.values())
print(list(dict1.keys()))
print(tuple(dict1.keys()))

print(dict1.items())###### 資料轉tuple
print(list(dict1.items()))
print(tuple(dict1.items()))

print('-----------------------------')
for key in dict1.keys():
    print(key)
print('-----------------------------')

for value in dict1.values():
    print(value)
print ( '-----------------------------' )
for data in dict1.items():
    print(data)


print('-----------------------------')
for key, value in dict1.items():
    print("{}:{}".format(key,value))