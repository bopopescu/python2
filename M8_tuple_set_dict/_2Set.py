set1 ={'python', 'java', 'c', 'c#'}
print(set1)
print(type(set1))

list1 = list(set1)
print(list1)
set1 = set(list1)
print(set1)
#上述戶轉

list1= {67,34,7,76,88,67}
set1= set(list1)
print(set1)#{34, 67, 7, 76, 88}
#print(set1[0])###'set' object does not support indexing
set1.add(88)#重複
print(set1)

set1.add(99)#
print(set1)
set1.remove(34)
print(set1)


